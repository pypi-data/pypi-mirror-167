# -*- coding: utf-8 -*-
"""
Core of the swe2hs algorithm.

Features of this version:
    - constant new snow density as model parameter
    - rho_max depending on overburden a layer has seen
    - switch to rho max wet when swe decreases?

"""

import numpy as np
from numba import njit

from swe2hs import __version__

__author__ = "Johannes Aschauer"
__copyright__ = "Johannes Aschauer"
__license__ = "GPL-3.0-or-later"


@njit
def _calculate_overburden(
    swe_layers: np.ndarray,
) -> np.ndarray:
    # reverse cumsum: https://stackoverflow.com/a/16541726
    # 50% SWE of the layer itself also contributes to overburden.
    return np.cumsum(swe_layers[::-1])[::-1] - swe_layers/2


@njit
def _adjust_rho_max_end_snowpack(
    rho_max_layers: np.ndarray,
    swe_layers: np.ndarray,
    rho_max_end: float,
    v_melt: float,
) -> np.ndarray:
    return np.where(
        swe_layers > 0,
        rho_max_end - (rho_max_end-rho_max_layers)*np.exp(-v_melt),
        rho_max_layers
    )


@njit
def _adjust_rho_max_based_on_overburden(
    rho_max_layers,
    overburden_layers,
    swe_layers,
    rho_max_init,
    rho_max_end,
    max_sigma
):
    """
    Calculate rho_max based on current overburden:
        - rho_max(ob=0) = rho_max_init
        - rho_max(ob=max_sigma) = rho_max_end
        - rho_max(ob>max_sigma) = rho_max_end
        - in between linear increase

    Parameters
    ----------
    rho_max_layers : :class:`numpy.ndarray`
        current maximum snow density in the layers
    overburden_layers : :class:`numpy.ndarray`
        overburden on the layers
    rho_max_init : float
        maximum density of "dry" snow.
    rho_max_end : float
        maximum density of "wet" snow.
    max_sigma : float
        overburden at which the density of wet snow is assumed.

    Returns
    -------
    :class:`numpy.ndarray`
        Adapted rho_max in the layers based on overburden
    """

    rho_max_current = np.zeros_like(overburden_layers)
    for i, o in enumerate(overburden_layers):
        if o >= max_sigma:
            rho_max_current[i] = rho_max_end
        else:
            rho_max_current[i] = ((rho_max_end-rho_max_init) /
                                  max_sigma)*o + rho_max_init

    updated_rho_max_layers = np.where((rho_max_current > rho_max_layers),
                                      rho_max_current,
                                      rho_max_layers)

    updated_rho_max_layers = np.where((swe_layers > 0), updated_rho_max_layers, 0.)

    return updated_rho_max_layers


@njit
def _remove_swe_from_top(
    swe_layers: np.ndarray,
    delta_swe: float
) -> np.ndarray:
    """
    Remove SWE from top of the layers in order to compesate for a loss in SWE
    (i.e. negative `delta_swe`).

    Parameters
    ----------
    swe_layers : :class:`numpy.ndarray`
    delta_swe : float

    Returns
    -------
    :class:`numpy.ndarray`
        updated SWE in the layers
    """
    swe_removed = 0
    l = len(swe_layers)-1
    # melting from top means going backward in layers.
    while swe_removed > delta_swe:  # both are (or will be) negative
        swe_removed = swe_removed - swe_layers[l]
        swe_layers[l] = 0
        l = l-1
        # minimal floating point errors can cause the while loop to
        # run away, in that case we force it to stop at bottom of the
        # snowpack.
        if l == -1:
            break
    # fill up last removed layer with excess swe:
    excess_swe = delta_swe - swe_removed
    if excess_swe > 0:
        swe_layers[l+1] = excess_swe
    return swe_layers


@njit
def timestep_forward(
    delta_swe,
    swe_layers,
    rho_layers,
    rho_max_layers,
    rho_new,
    rho_max_init,
    rho_max_end,
    R,
    max_sigma,
    v_melt,
):
    """Process a timestep forward.

    Assumes that an empty new layer has already been created at the end of
    each of the layer arrays where the function can write values to. This 
    padding at the end can be done with :func:`pad_layer_arrays_with_zero`.

    """

    if delta_swe > 0:
        swe_layers[-1] = delta_swe
        rho_layers[-1] = rho_max_init

    if delta_swe < 0:
        swe_layers = _remove_swe_from_top(swe_layers, delta_swe)
        rho_max_layers = _adjust_rho_max_end_snowpack(
            rho_max_layers,
            swe_layers,
            rho_max_end,
            v_melt,
        )

    overburden_layers = _calculate_overburden(swe_layers)
    # update rho_max based on overburden: should not be reversible.
    rho_max_layers = _adjust_rho_max_based_on_overburden(
        rho_max_layers,
        overburden_layers,
        swe_layers,
        rho_max_init,
        rho_max_end,
        max_sigma
    )

    # update rho, i.e. calculate settling:
    rho_layers = np.where(
        (swe_layers > 0),
        rho_max_layers - (rho_max_layers-rho_layers) * np.exp(-1/R),
        0.)

    if delta_swe > 0:
        # rho_new should not get modified in the first timestep.
        rho_layers[-1] = rho_new
        rho_max_layers[-1] = rho_max_init

    return swe_layers, rho_layers, rho_max_layers


@njit
def _set_layer_states_nan(swe_layers, rho_layers, rho_max_layers):
    swe_layers = np.full_like(swe_layers, np.nan)
    rho_layers = np.full_like(rho_layers, np.nan)
    rho_max_layers = np.full_like(rho_max_layers, np.nan)
    return swe_layers, rho_layers, rho_max_layers


@njit
def _calculate_hs_layers(swe_layers, rho_layers):
    """Loop to avoid division by zero"""
    hs_layers = np.zeros(len(swe_layers), dtype='float64')
    for i, (swe, rho) in enumerate(zip(swe_layers, rho_layers)):
        if swe > 0:
            hs_layers[i] = swe*1000 / rho
    return hs_layers


@njit
def _nansum_numba(array):
    """
    Looped numba version faster than np.nansum

    Parameters
    ----------
    array : :class:`numpy.ndarray`
        1 dimensional ndarray, float dtype

    Returns
    -------
    sum : float
    """
    sum = 0.
    for x in array:
        if np.isnan(x):
            continue
        else:
            sum += x
    return sum


@njit
def _pad_end_of_array_with_zero(array):
    # np.pad not supported in numba, we need some ugly hacking.
    # https://github.com/numba/numba/issues/4074
    padded = np.zeros(len(array)+1, dtype='float64')
    padded[:-1] = array
    return padded


@njit
def _pad_layer_arrays_with_zero(
    swe_layers_in,
    rho_layers_in,
    rho_max_layers_in,
):
    swe_layers_mod = _pad_end_of_array_with_zero(swe_layers_in)
    rho_layers_mod = _pad_end_of_array_with_zero(rho_layers_in)
    rho_max_layers_mod = _pad_end_of_array_with_zero(rho_max_layers_in)
    return swe_layers_mod, rho_layers_mod, rho_max_layers_mod


@njit
def swe2hs_snowpack_evolution(
    swe_input,
    rho_new,
    rho_max_init,
    rho_max_end,
    R,
    max_sigma,
    v_melt,  # should be in range 0.1 - 2.0
):
    """
    Snowpack evolution within the swe2hs model.

    Meant to be called on single hydrological years or chunks of nonzeros
    """

    # allocate output arrays:
    hs_out = np.zeros(len(swe_input))
    hs_layers_out = np.zeros((len(swe_input), len(swe_input)))
    rho_layers_out = np.zeros((len(swe_input), len(swe_input)))
    rho_max_layers_out = np.zeros((len(swe_input), len(swe_input)))

    # allocate layer containers
    swe_layers = np.zeros(0)  # tracking of swe
    rho_layers = np.zeros(0)  # tracking of density
    rho_max_layers = np.zeros(0)  # tracking of maximum density

    # iterate through input array.
    for i, swe in enumerate(swe_input):

        swe_layers, rho_layers, rho_max_layers = _pad_layer_arrays_with_zero(
            swe_layers,
            rho_layers,
            rho_max_layers,
        )

        if np.isnan(swe):
            swe_layers, rho_layers, rho_max_layers = _set_layer_states_nan(
                swe_layers,
                rho_layers,
                rho_max_layers
            )
            hs_out[i] = np.nan
            continue

        # Force HS to zero when SWE is zero in order to avoid floating point
        # artifacts after a snowpack evolution.
        if swe == 0:
            swe_layers, rho_layers, rho_max_layers = _set_layer_states_nan(
                swe_layers,
                rho_layers,
                rho_max_layers
            )
            hs_out[i] = 0.
            continue

        # get delta swe:
        if i == 0:
            delta_swe = swe
        else:
            delta_swe = swe - swe_input[i-1]

        swe_layers, rho_layers, rho_max_layers = timestep_forward(
            delta_swe,
            swe_layers,
            rho_layers,
            rho_max_layers,
            rho_new,
            rho_max_init,
            rho_max_end,
            R,
            max_sigma,
            v_melt,
        )

        hs_layers = _calculate_hs_layers(swe_layers, rho_layers)

        hs_out[i] = _nansum_numba(hs_layers)

        hs_layers_out[:i+1, i] = hs_layers

        rho_max_layers_out[:i+1, i] = rho_max_layers
        rho_layers_out[:i+1, i] = rho_layers

    return hs_out, hs_layers_out, rho_layers_out, rho_max_layers_out


@njit
def swe2hs_snowpack_evolution_return_no_layer_states(
    swe_input,
    rho_new,
    rho_max_init,
    rho_max_end,
    R,
    max_sigma,
    v_melt,  # should be in range 0.1 - 2.0
):
    """
    Snowpack evolution within the swe2hs model.

    Meant to be called on single hydrological years or chunks of nonzeros
    """

    # allocate output arrays:
    hs_out = np.zeros(len(swe_input))

    # allocate layer containers
    swe_layers = np.zeros(0)  # tracking of swe
    rho_layers = np.zeros(0)  # tracking of density
    rho_max_layers = np.zeros(0)  # tracking of maximum density

    # iterate through input array.
    for i, swe in enumerate(swe_input):

        if np.isnan(swe):
            # reset layer varibales
            swe_layers = np.zeros(0)
            rho_layers = np.zeros(0)
            rho_max_layers = np.zeros(0)
            hs_out[i] = np.nan
            continue

        # Force HS to zero when SWE is zero in order to avoid floating point
        # artifacts after a snowpack evolution.
        if swe == 0:
            # reset layer varibales
            swe_layers = np.zeros(0)
            rho_layers = np.zeros(0)
            rho_max_layers = np.zeros(0)
            hs_out[i] = 0.
            continue

        swe_layers, rho_layers, rho_max_layers = _pad_layer_arrays_with_zero(
            swe_layers,
            rho_layers,
            rho_max_layers,
        )

        # get delta swe:
        if i == 0:
            delta_swe = swe
        else:
            delta_swe = swe - swe_input[i-1]

        swe_layers, rho_layers, rho_max_layers = timestep_forward(
            delta_swe,
            swe_layers,
            rho_layers,
            rho_max_layers,
            rho_new,
            rho_max_init,
            rho_max_end,
            R,
            max_sigma,
            v_melt,
        )

        hs_layers = _calculate_hs_layers(swe_layers, rho_layers)

        hs_out[i] = _nansum_numba(hs_layers)

    return hs_out

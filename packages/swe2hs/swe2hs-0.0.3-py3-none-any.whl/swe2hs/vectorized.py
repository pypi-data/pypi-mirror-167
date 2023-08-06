import numpy as np
import xarray as xr
import dask.array as da
from numba import guvectorize

from .core import swe2hs_snowpack_evolution_return_no_layer_states
from .utils import (
    continuous_timedeltas,
    get_nonzero_chunk_idxs,
    _get_split_indices_based_on_date,
)

from ._default_model_parameters import *


@guvectorize(
    ['void(float64[:], int64[:], float64, float64, float64, float64, float64, float64, int64, int64, float64[:])'],
    '(n),(n),(),(),(),(),(),(),(),()->(n)',
    nopython=True
)
def _swe2hs_gufunc_reset_day(
    swe_input,
    month_input,
    rho_new,
    rho_max_init,
    rho_max_end,
    R,
    max_sigma,
    v_melt,
    split_month,
    split_day,
    hs_out,
):
    """
    Numba gufunc which resets the snowpack when day and month both match the
    split_day and split_month arguments.
    """
    split_idxs = _get_split_indices_based_on_date(month_input, split_month, split_day)

    for start, stop in zip(split_idxs[:-1], split_idxs[1:]):
        hs_out[start:stop] = swe2hs_snowpack_evolution_return_no_layer_states(
            swe_input[start:stop],
            rho_new,
            rho_max_init,
            rho_max_end,
            R,
            max_sigma,
            v_melt,
        )


@guvectorize(
    ['void(float64[:], float64, float64, float64, float64, float64, float64, float64[:])'],
    '(n),(),(),(),(),(),()->(n)',
    nopython=True
)
def _swe2hs_gufunc_no_reset_day(
    swe_input,
    rho_new,
    rho_max_init,
    rho_max_end,
    R,
    max_sigma,
    v_melt,
    hs_out,
):
    """
    Numba gufunc which splits swe input into chunks of consecutive nonzeros and 
    calculates swe2hs on these chunks. 
    """
    hs_out[:] = swe2hs_snowpack_evolution_return_no_layer_states(
        swe_input,
        rho_new,
        rho_max_init,
        rho_max_end,
        R,
        max_sigma,
        v_melt,
    )


def _wrapped_swe2hs_gufunc_reset_day(
    swe_input,
    month_input,
    rho_new=RHO_NEW,
    rho_max_init=RHO_MAX_INIT,
    rho_max_end=RHO_MAX_END,
    R=R,
    max_sigma=MAX_SIGMA,
    v_melt=V_MELT,
    split_month=9,
    split_day=1,
):
    """
    Wrap the gufunc in order to accept keyword arguments.
    """
    # initialize output
    hs_out = np.zeros(len(swe_input), dtype=np.float64)

    with np.errstate(invalid='ignore'):
        # call vetorized function
        hs_out = _swe2hs_gufunc_reset_day(
            swe_input,
            month_input,
            rho_new,
            rho_max_init,
            rho_max_end,
            R,
            max_sigma,
            v_melt,
            split_month,
            split_day,
        )
    return hs_out


def _wrapped_swe2hs_gufunc_no_reset_day(
    swe_input,
    rho_new=RHO_NEW,
    rho_max_init=RHO_MAX_INIT,
    rho_max_end=RHO_MAX_END,
    R=R,
    max_sigma=MAX_SIGMA,
    v_melt=V_MELT,
):
    """
    Wrap the gufunc in order to accept keyword arguments.
    """
    # initialize output
    hs_out = np.zeros(len(swe_input), dtype=np.float64)
    # we have problems with nans for .core._calculate_hs_layers
    # see https://github.com/numba/numba/issues/4793#issuecomment-622323686
    with np.errstate(invalid='ignore'):
        # call vetorized function
        hs_out = _swe2hs_gufunc_no_reset_day(
            swe_input,
            rho_new,
            rho_max_init,
            rho_max_end,
            R,
            max_sigma,
            v_melt,
        )
    return hs_out


def apply_swe2hs(
    swe_data,
    rho_new=RHO_NEW,
    rho_max_init=RHO_MAX_INIT,
    rho_max_end=RHO_MAX_END,
    R=R,
    max_sigma=MAX_SIGMA,
    v_melt=V_MELT,
    time_dim_name='time',
    reset_day=None,
):
    """
    Distributed version of the swe2hs model. 

    Apply the model on a :class:`xarray.DataArray` which holds three
    dimensional SWE data (x dimension, y dimension and time dimension).

    This function calls a numba guvectorized version of swe2hs within
    :func:`xarray.apply_ufunc`.

    If you pass a :class:`xarray.DataArray` containing Dask data arrays which
    are chunked in the x (lon) and y (lat) dimensions, this function will
    execute the model in parallel over the different chunks. If you additionally
    read and write from a netcdf file in chunks, you can process datasets which
    would normally not fit into memory. 

    Parameters
    ----------
    swe_data : :class:`xarray.DataArray`
        DataArray containing the SWE data in [m].
    rho_new : float, optional
        New snow density in [kg/m^3], by default 85.9138139656343.
    rho_max_init : float, optional
        Initial value of the maximum snow density of a layer in [kg/m^3], by
        default 204.1345890849816.
    rho_max_end : float, optional
        End value of the maximum snow density of a layer in [kg/m^3], by 
        efault 427.1806327485636.
    R : float, optional
        Settling resistance, by default 5.922898941101872.
    max_sigma : float, optional
        Overburden where rho_max reaches rho_max,end, by default 
        0.2269148577394744.
    v_melt : float, optional
        Speed of the transition towards rho_max,end in case of global SWE
        decrease, by default 0.13355554554152269
    time_dim_name : str, optional
        Name of the time dimension in the input SWE data, by default 'time'.
    reset_day : str or None, optional
        Day in the year where the model state is getting reset of the format 
        'MM-DD'. If set to None, the model state will never be reset. The
        default is None.


    Returns
    -------
    :class:`xarray.DataArray
        Calculated snow depth, same format as the input data.

    Raises
    ------
    ValueError
        If any of the constraints on the data are violated. 
    """
    if not isinstance(swe_data, xr.DataArray):
        raise TypeError("swe2hs: swe data needs to be a xarray.DataArray.")

    input_dims = swe_data.dims

    if time_dim_name not in input_dims:
        raise ValueError(("swe2hs: you assigned the time dimension name "
                          f"'{time_dim_name}' which is \nnot in the dimensions "
                          "of the SWE input DataArray."))

    # pass parameters to a dict for later reuse
    params = {
        'rho_new': rho_new,
        'rho_max_init': rho_max_init,
        'rho_max_end': rho_max_end,
        'R': R,
        'max_sigma': max_sigma,
        'v_melt': v_melt,
    }

    if reset_day is not None:
        contiuous, resolution = continuous_timedeltas(swe_data[time_dim_name].values)
        if not contiuous or resolution != 24:
            raise ValueError(
                (f"swe2hs: time dimension '{time_dim_name}' is not continuous "
                 "or does not have 1 day resolution.")
            )

        split_month = int(reset_day.split('-')[0])
        split_day = int(reset_day.split('-')[1])
        params.update({'split_month': split_month, 'split_day': split_day})

    if isinstance(swe_data.data, np.ndarray):
        if reset_day is None:
            hs = (xr
                  .apply_ufunc(
                      _wrapped_swe2hs_gufunc_no_reset_day,
                      swe_data,
                      kwargs=params,
                      input_core_dims=[[time_dim_name]],
                      output_core_dims=[[time_dim_name]],
                  )
                  )
        else:
            hs = (xr
                  .apply_ufunc(
                      _wrapped_swe2hs_gufunc_reset_day,
                      swe_data,
                      swe_data.coords[f'{time_dim_name}.month'],
                      kwargs=params,
                      input_core_dims=[[time_dim_name], [time_dim_name]],
                      output_core_dims=[[time_dim_name]],
                )
            )
    elif isinstance(swe_data.data, da.core.Array):
        if reset_day is None:
            hs = (xr
                  .apply_ufunc(
                      _wrapped_swe2hs_gufunc_no_reset_day,
                      swe_data,
                      kwargs=params,
                      input_core_dims=[[time_dim_name]],
                      output_core_dims=[[time_dim_name]],
                      dask='parallelized',
                      output_dtypes=['float64']
                  )
                  )
        else:
            hs = (xr
                  .apply_ufunc(
                      _wrapped_swe2hs_gufunc_reset_day,
                      swe_data,
                      swe_data.coords[f'{time_dim_name}.month'],
                      kwargs=params,
                      input_core_dims=[[time_dim_name], [time_dim_name]],
                      output_core_dims=[[time_dim_name]],
                      dask='parallelized',
                      output_dtypes=['float64']
                )
            )
    else:
        raise TypeError(("swe2hs: underlying data in the xr.DataArray needs to "
                         "be numpy.ndarray or dask array."))

    return hs.transpose(input_dims[0], input_dims[1], input_dims[2])

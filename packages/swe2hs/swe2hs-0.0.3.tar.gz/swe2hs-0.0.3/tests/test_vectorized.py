import pytest
import numpy as np
import pandas as pd
import xarray as xr


from swe2hs.one_dimensional import swe2hs_1d
from swe2hs.vectorized import (
    apply_swe2hs,
    _swe2hs_gufunc_no_reset_day,
    _swe2hs_gufunc_reset_day,
    _wrapped_swe2hs_gufunc_no_reset_day,
    _wrapped_swe2hs_gufunc_reset_day,
)


def test_swe2hs_gufunc_against_1d_version_no_reset_day(swe_data_1d_series, default_swe2hs_params):
    params = default_swe2hs_params
    from_1d = swe2hs_1d(swe_data_1d_series, **params)

    from_gufunc = pd.Series(
        data=_swe2hs_gufunc_no_reset_day(
            swe_data_1d_series.to_numpy(),
            params['rho_new'],
            params['rho_max_init'],
            params['rho_max_end'],
            params['R'],
            params['max_sigma'],
            params['v_melt'],
        ),
        index=swe_data_1d_series.index
    )
    pd.testing.assert_series_equal(from_1d, from_gufunc)


def test_swe2hs_gufunc_against_1d_version_reset_day(swe_data_1d_series, default_swe2hs_params):
    params = default_swe2hs_params
    from_1d = swe2hs_1d(swe_data_1d_series, **params)

    from_gufunc = pd.Series(
        data=_swe2hs_gufunc_reset_day(
            swe_data_1d_series.to_numpy(),
            swe_data_1d_series.index.month.to_numpy(),
            params['rho_new'],
            params['rho_max_init'],
            params['rho_max_end'],
            params['R'],
            params['max_sigma'],
            params['v_melt'],
            9,
            2,
        ),
        index=swe_data_1d_series.index
    )

    pd.testing.assert_series_equal(from_1d, from_gufunc)


def test_wrapped_swe2hs_gufunc_against_1d_version_no_reset_day(swe_data_1d_series, default_swe2hs_params):
    from_1d = swe2hs_1d(
        swe_data_1d_series,
        **default_swe2hs_params
        )

    from_call = pd.Series(
        data=_wrapped_swe2hs_gufunc_no_reset_day(
            swe_data_1d_series.to_numpy(),
            **default_swe2hs_params
            ),
        index=swe_data_1d_series.index
        )

    pd.testing.assert_series_equal(from_1d, from_call)


def test_wrapped_swe2hs_gufunc_against_1d_version_reset_day(swe_data_1d_series, default_swe2hs_params):
    from_1d = swe2hs_1d(
        swe_data_1d_series,
        **default_swe2hs_params
    )

    from_call = pd.Series(
        data=_wrapped_swe2hs_gufunc_reset_day(
            swe_data_1d_series.to_numpy(),
            swe_data_1d_series.index.month.to_numpy(),
            split_month=9,
            split_day=2,
            **default_swe2hs_params
        ),
        index=swe_data_1d_series.index
    )

    pd.testing.assert_series_equal(from_1d, from_call)


@pytest.mark.parametrize(
    "reset_day",
    [(None), ('09-02'), ]
)
def test_apply_swe2hs_dask_vs_numpy(
    reset_day,
    swe_data_2d_dataarray_numpy,
    swe_data_2d_dataarray_dask,
    default_swe2hs_params
):
    numpy_result = apply_swe2hs(swe_data_2d_dataarray_numpy,
                                reset_day=reset_day, **default_swe2hs_params)
    dask_result = apply_swe2hs(swe_data_2d_dataarray_dask,
                               reset_day=reset_day, **default_swe2hs_params)

    xr.testing.assert_allclose(numpy_result, dask_result)


@pytest.mark.parametrize(
    "swe_dataarray",
    [
        ("swe_data_2d_dataarray_numpy"),
        ("swe_data_2d_dataarray_dask"),
        ("swe_data_2d_dataarray_numpy_changed_dimorder"),
    ],
)
@pytest.mark.parametrize(
    "reset_day",
    [(None), ('09-02'), ]
)
def test_apply_swe2hs_against_1d(
    swe_dataarray,
    reset_day,
    swe_data_1d_series,
    default_swe2hs_params,
    request
):
    swe_da = request.getfixturevalue(swe_dataarray)
    hs_da = apply_swe2hs(swe_data=swe_da, reset_day=reset_day, **default_swe2hs_params)
    hs_series = swe2hs_1d(swe_data_1d_series, **default_swe2hs_params)

    # 1.) check if 1d equals the lon=0 and lat=0 pixel.
    pd.testing.assert_series_equal(
        hs_da.sel(lat=0, lon=0).to_pandas(),
        hs_series,
        check_names=False,
        check_freq=False,
        )
    # 2.) check if the lon=0 and lat=0 pixel equals all other pixels
    assert (hs_da == hs_da.sel(lat=0, lon=0)).all()


@pytest.mark.parametrize(
    "swe_dataarray",
    [
        ("swe_data_2d_dataarray_numpy"),
        ("swe_data_2d_dataarray_dask"),
        ("swe_data_2d_dataarray_numpy_changed_dimorder"),
    ],
)
def test_dimension_preservation_in_apply_swe2hs(
    swe_dataarray,
    default_swe2hs_params,
    request
):
    swe_da = request.getfixturevalue(swe_dataarray)
    hs_da = apply_swe2hs(swe_data=swe_da, **default_swe2hs_params)

    assert swe_da.dims == hs_da.dims


@pytest.mark.parametrize(
    "reset_day",
    [(None), ('09-02'), ]
)
def test_single_nan_cell(
    reset_day,
    swe_data_1d_series,
    swe_data_2d_dataarray_numpy_one_cell_nan,
    default_swe2hs_params
):
    hs_da = apply_swe2hs(
        swe_data=swe_data_2d_dataarray_numpy_one_cell_nan, reset_day=reset_day, **default_swe2hs_params)
    hs_series = swe2hs_1d(swe_data_1d_series, **default_swe2hs_params)

    # check if lon=0 and lat=0 pixel is all nan
    assert np.all(np.isnan(hs_da.sel(lon=0, lat=0)))

    for lat in hs_da.coords['lat']:
        for lon in hs_da.coords['lon']:
            if lat == 0 and lon == 0:
                continue
            else:
                pd.testing.assert_series_equal(
                    hs_da.sel(lat=lat, lon=lon).to_pandas(),
                    hs_series,
                    check_names=False,
                    check_freq=False,
                )


@pytest.mark.parametrize(
    "swe_dataarray",
    [
        ("swe_data_2d_dataarray_numpy_nans_in_june"),
    ],
)
def test_apply_swe2hs_against_1d_nans_in_june(
    swe_dataarray,
    swe_data_1d_series_nans_in_june,
    default_swe2hs_params,
    request
):
    swe_da = request.getfixturevalue(swe_dataarray)
    hs_da = apply_swe2hs(swe_data=swe_da, **default_swe2hs_params)
    hs_series = swe2hs_1d(
        swe_data_1d_series_nans_in_june,
        ignore_zeropadded_gaps=True,
        **default_swe2hs_params)

    for lat in hs_da.coords['lat']:
        for lon in hs_da.coords['lon']:
            pd.testing.assert_series_equal(
                hs_da.sel(lat=lat, lon=lon).to_pandas(),
                hs_series,
                check_names=False,
                check_freq=False,
            )


@pytest.mark.parametrize(
    "swe_dataarray",
    [
        ("swe_data_2d_dataarray_numpy"),
        ("swe_data_2d_dataarray_dask"),
        ("swe_data_2d_dataarray_numpy_changed_dimorder"),
    ],
)
def test_apply_swe2hs_reset_day(
    swe_dataarray,
    request,
):
    swe_da = request.getfixturevalue(swe_dataarray)

    hs1 = apply_swe2hs(swe_data=swe_da, reset_day=None)
    hs2 = apply_swe2hs(swe_data=swe_da, reset_day='09-02')

    xr.testing.assert_allclose(hs1, hs2)

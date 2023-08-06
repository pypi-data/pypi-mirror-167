---
file_format: mystnb
kernelspec:
  name: python3
---

# Using the one dimensional model version

This notebook describes how to use the one dimensional version of the SWE2HS model. You can transfer a [`pandas.Series`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html) which contain daily snow water equivalent of the snowpack (SWE) to a `pandas.Series` of daily snow depth (HS). The series must have a [`pandas.DatetimeIndex`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DatetimeIndex.html?highlight=datetimeindex#pandas.DatetimeIndex) as index.

First import some libraries...

```{code-cell}
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
```

... and import the necessary functions from the SWE2HS package

```{code-cell}
from swe2hs.one_dimensional import swe2hs_1d
from swe2hs.visualization import layer_plot
```

Let us create some dummy SWE data. For this we create a function which defines an artificial SWE evolution for a single winter an inject it at the first of December repeatedly for a given number of years `n_years`. 

```{code-cell}
def create_swe(n_years):
    dates = pd.date_range(start='2000-07-01', end=f'{2000+n_years}-06-30', freq='D')
    swe = np.zeros(len(dates))
    swe_winter = np.array([0.01]*10 + [0.02]*5 + [0.1]*10 + [0.15]*10 + np.linspace(
        0.15, 0.1, 10).tolist() + [0.25]*20 + [0.35]*15 + np.linspace(0.35, 0., 50).tolist())
    first_decembers = np.nonzero(dates.strftime('%m-%d') == '12-01')[0]
    for f in first_decembers:
        swe[f:f+len(swe_winter)] = swe_winter
    return pd.Series(swe, index=dates, name='SWE [m]')
```

For the example we create data of three years.

```{code-cell}
swe = create_swe(n_years=3)
swe.plot()
```

Now we convert the SWE series to HS with the `swe2hs_1d` function:

```{code-cell}
hs = swe2hs_1d(swe, swe_input_unit='m', hs_output_unit='m')
hs.plot()
```

### Layer plot

Now we want to plot the layer evolution within the modelled snowpack. For this we create only one year of SWE data.

```{code-cell}
swe_one_year = create_swe(n_years=1)
```

When we call the `swe2hs_1d` function with `return_layers=True`, it will return an [`xarray.Dataset`](https://docs.xarray.dev/en/stable/generated/xarray.Dataset.html) where the layer state variables are stored alongside the snow depth.

```{code-cell}
hs_with_layers = swe2hs_1d(swe_one_year, return_layers=True)
hs_with_layers
```

We can plot the layer evolution with the `layer_plot` function from the visualization module. Here we choose to display the layer color to be mapped to the density of the layers.

```{code-cell}
fig, ax = plt.subplots()
layer_plot(
    ax, 
    hs_with_layers, 
    color_variable='layer_densities', 
    cbar_label='Density [kg m$^{-3}$]'
)
plt.show()
```
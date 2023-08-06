================
Module Reference
================


One dimensional version
=======================

.. automodule:: swe2hs.one_dimensional
.. currentmodule:: swe2hs.one_dimensional

.. autosummary::
   :toctree: _autosummary

   swe2hs_1d

Two dimensional distributed version
===================================

.. automodule:: swe2hs.vectorized
.. currentmodule:: swe2hs.vectorized

.. autosummary::
   :toctree: _autosummary

   apply_swe2hs

Two dimesnional step-by-step version
====================================

.. automodule:: swe2hs.operational
.. currentmodule:: swe2hs.operational

.. autosummary::
   :toctree: _autosummary

   process_timestep_from_nc_files



Datetime and Gap Detection Utils
================================

.. automodule:: swe2hs.utils
.. currentmodule:: swe2hs.utils

.. autosummary::
   :toctree: _autosummary

   continuous_timedeltas
   continuous_timedeltas_in_nonzero_chunks
   fill_small_gaps
   get_nonzero_chunk_idxs
   get_small_gap_idxs
   get_zeropadded_gap_idxs


Core of the model
=================

.. automodule:: swe2hs.core
.. currentmodule:: swe2hs.core

.. autosummary::
   :toctree: _autosummary

   timestep_forward
   swe2hs_snowpack_evolution
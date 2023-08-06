SWE2HS Documentation
====================

.. image:: https://img.shields.io/gitlab/pipeline-status/aschauer/swe2hs?branch=master&gitlab_url=https%3A%2F%2Fgitlabext.wsl.ch&label=Pipeline Status
   :alt: Gitlab pipeline status (self-hosted)
   :target: https://code.wsl.ch/aschauer/swe2hs/-/commits/master

.. image:: https://img.shields.io/pypi/v/swe2hs.svg
        :alt: PyPI-Server
        :target: https://pypi.org/project/swe2hs/

.. image:: https://img.shields.io/pypi/pyversions/swe2hs
    :alt: PyPI - Python Version

|

This is the documentation of SWE2HS, a conceptual model to transfer snow water
equivalent of the snow cover to snow depth. Some people informally call it JOPACK,
which is obviously an acronym for Just Density Of the snowPACK. 

The density model calculates snow depth (HS) on a daily resolution and is 
driven by the daily snow water equivalent (SWE) of the snow cover only. The 
model creates a new layer with a fixed new snow density :math:`\rho_{new}` for 
every increase in SWE and a snowpack of individual layers builds up. Subsequently, 
the density of a layer increases with time towards a theoretical maximum 
density. The maximum density is starting with an initial value at creation 
time of the layer and is subsequently gravitating towards a higher end value 
based on the overburden a layer has experienced and the occurrence of SWE 
losses in the snow pack. When SWE decreases, the model removes SWE from the 
top of the snowpack. The layer number :math:`n` can thus undergo changes over time 
based on the number of SWE increases and losses in the snowpack. The model 
neglects constructive metamorphism, refreezing and is not able to capture 
rain-on-snow (ROS) events which might lead to an increase in SWE but no 
increase in HS. 

|

.. image:: _static/colored_layers_kuhtai_2002.png
   :alt: Schematic snowpack evolution

The figure shows the schematic modeled snow pack evolution for the station 
Kuhtai in the winter 2001/02. The red dotted line is the measured snow depth 
(HS), the black solid line bounding the colored area is the modeled snow depth, 
the thin black lines depict the layer borders within the modeled snowpack, and 
the coloring refers to the modeled layer densities. The bottom panel shows the 
daily snow water equivalent time series which was used to force the model.

|

Contents
========

.. toctree::
   :maxdepth: 2

   Getting started <getting_started>
   Examples <examples>
   Contributing <contributing>
   Module Reference <api>




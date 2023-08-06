.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

.. image:: https://img.shields.io/badge/Documentation-blue
    :alt: Documentation
    :target: https://aschauer.gitlab-pages.wsl.ch/swe2hs/

.. image:: https://img.shields.io/gitlab/pipeline-status/aschauer/swe2hs?branch=master&gitlab_url=https%3A%2F%2Fgitlabext.wsl.ch&label=Pipeline Status
   :alt: Gitlab pipeline status (self-hosted)
   :target: https://code.wsl.ch/aschauer/swe2hs/-/commits/master

.. image:: https://img.shields.io/pypi/v/swe2hs.svg
        :alt: PyPI-Server
        :target: https://pypi.org/project/swe2hs/

.. image:: https://img.shields.io/pypi/pyversions/swe2hs
    :alt: PyPI - Python Version



*This project is work in progress.*

======
swe2hs
======


A simple conceptual snow density model for transferring snow water equivalent
to snow depth, some people informally call it JoPack.

The density model calculates snow depth (HS) on a daily resolution and is
driven by daily water equivalent of the snow cover (SWE). The model
creates a new layer with a constant new snow density for every increase in
SWE and a snowpack of individual layers builds up. The density of a layer
increases towards a theoretical maximum density depending on an interaction of
overburden acting on the layer and the current density of the layer. The
maximum density is starting with an initial value at creation time of the
layer and is subsequently gravitating towards a higher end value based on the
overburden a layer has experienced and the occurrence of negative global SWE
changes. When SWE decreases, the model entirely or partly removes layers from
top of the snowpack until the loss in SWE is compensated.


============================
Installation and development
============================


Clone the repository::

    $ git clone https://gitlabext.wsl.ch/aschauer/swe2hs.git

A new directory `swe2hs` will be created. After navigating to this directory,
you can use::

    $ pip install .

If you want to make changes to the package, install it in editable mode with::

    $ pip install -e .

Testing is done with tox. Assuming you are in the root directory, run the tests
with::

    $ tox

You can also run individual tests from a single module with::

    $ tox tests/test_module.py

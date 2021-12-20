
========
WARNING
========
This is still very much a work in progress and nothing can be assumed stable in any way


Temp notes:

Two types of created installer, based on whether it contains:

1. All dependencies (conda, R, R packages, Shiny app, etc)
2. Strict instructions for dependency install



========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - tests
      - | |github-actions|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |github-actions| image:: https://github.com/chasemc/duplipy/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/chasemc/duplipy/actions

.. |codecov| image:: https://codecov.io/gh/chasemc/duplipy/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://codecov.io/github/chasemc/duplipy

.. |version| image:: https://img.shields.io/pypi/v/duplipy.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/duplipy

.. |wheel| image:: https://img.shields.io/pypi/wheel/duplipy.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/duplipy

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/duplipy.svg
    :alt: Supported versions
    :target: https://pypi.org/project/duplipy

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/duplipy.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/duplipy

.. |commits-since| image:: https://img.shields.io/github/commits-since/chasemc/duplipy/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/chasemc/duplipy/compare/v0.0.0...main



.. end-badges

Create standalone, installable R Shiny apps using Electron

* Free software: MIT license

Installation
============

::

    pip install duplipy

You can also install the in-development version with::

    pip install https://github.com/chasemc/duplipy/archive/main.zip


Documentation
=============


To use the project:

.. code-block:: python

    import duplipy
    duplipy.longest()


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox

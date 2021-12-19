
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

.. |github-actions| image:: https://github.com/chasemc/electricpy/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/chasemc/electricpy/actions

.. |codecov| image:: https://codecov.io/gh/chasemc/electricpy/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://codecov.io/github/chasemc/electricpy

.. |version| image:: https://img.shields.io/pypi/v/electricpy.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/electricpy

.. |wheel| image:: https://img.shields.io/pypi/wheel/electricpy.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/electricpy

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/electricpy.svg
    :alt: Supported versions
    :target: https://pypi.org/project/electricpy

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/electricpy.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/electricpy

.. |commits-since| image:: https://img.shields.io/github/commits-since/chasemc/electricpy/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/chasemc/electricpy/compare/v0.0.0...main



.. end-badges

Create standalone, installable R Shiny apps using Electron

* Free software: MIT license

Installation
============

::

    pip install electricpy

You can also install the in-development version with::

    pip install https://github.com/chasemc/electricpy/archive/main.zip


Documentation
=============


To use the project:

.. code-block:: python

    import electricpy
    electricpy.longest()


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

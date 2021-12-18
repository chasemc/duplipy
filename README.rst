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

.. |github-actions| image:: https://github.com/chasemc/electricpie/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/chasemc/electricpie/actions

.. |codecov| image:: https://codecov.io/gh/chasemc/electricpie/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://codecov.io/github/chasemc/electricpie

.. |version| image:: https://img.shields.io/pypi/v/electricpie.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/electricpie

.. |wheel| image:: https://img.shields.io/pypi/wheel/electricpie.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/electricpie

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/electricpie.svg
    :alt: Supported versions
    :target: https://pypi.org/project/electricpie

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/electricpie.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/electricpie

.. |commits-since| image:: https://img.shields.io/github/commits-since/chasemc/electricpie/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/chasemc/electricpie/compare/v0.0.0...main



.. end-badges

Create standalone, installable R Shiny apps using Electron

* Free software: MIT license

Installation
============

::

    pip install electricpie

You can also install the in-development version with::

    pip install https://github.com/chasemc/electricpie/archive/main.zip


Documentation
=============


To use the project:

.. code-block:: python

    import electricpie
    electricpie.longest()


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

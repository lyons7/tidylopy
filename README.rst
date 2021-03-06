.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/<USER>/tidylopy.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/<USER>/tidylopy
    .. image:: https://readthedocs.org/projects/tidylopy/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://tidylopy.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/coveralls/github/<USER>/tidylopy/main.svg
        :alt: Coveralls
        :target: https://coveralls.io/r/<USER>/tidylopy
    .. image:: https://img.shields.io/pypi/v/tidylopy.svg
        :alt: PyPI-Server
        :target: https://pypi.org/project/tidylopy/
    .. image:: https://img.shields.io/conda/vn/conda-forge/tidylopy.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/tidylopy
    .. image:: https://pepy.tech/badge/tidylopy/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/tidylopy
    .. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
        :alt: Twitter
        :target: https://twitter.com/tidylopy

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

|

========
tidylopy
========


    Python adaptation of Python adaptation of Schnoebelen, Silge and Hayes's (2020) `tidylo <https://github.com/juliasilge/tidylo>`_ R library




Nothing fancy -- I'm a huge fan of the new `tidylo <https://github.com/juliasilge/tidylo>`_ R library and wanted to be able to replicate the default ``bind_log_odds`` function in Python! The function is located in `src/tidylopy <https://github.com/lyons7/tidylopy/blob/main/src/tidylopy/tidylopy.py>`_, and the `examples <https://github.com/lyons7/tidylopy/tree/main/examples>`_ folder has a .ipynb notebook demonstrating how to use it + compares results on the same data of ``bind_log_odds`` from tidylo and ``get_weighted_log_odds`` from tidylopy!


.. _pyscaffold-notes:

Note
====

This project has been set up using PyScaffold 4.1.4. For details and usage
information on PyScaffold see https://pyscaffold.org/.

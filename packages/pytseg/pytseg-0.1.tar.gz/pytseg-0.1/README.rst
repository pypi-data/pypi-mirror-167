*****************************************
Time series segmentation toolbox (pytseg)
*****************************************

.. image:: https://github.com/RaoulHeese/pytseg/actions/workflows/tests.yml/badge.svg
    :target: https://github.com/RaoulHeese/pytseg/actions/workflows/tests.yml
    :alt: GitHub Actions
	
.. image:: https://readthedocs.org/projects/pytseg/badge/?version=latest
    :target: https://pytseg.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status	
	
.. image:: https://img.shields.io/pypi/pyversions/pytseg
    :target: https://pypi.org/project/pytseg/
    :alt: PyPI Versions
	
.. image:: https://img.shields.io/badge/license-MIT-lightgrey
    :target: https://github.com/RaoulHeese/pytseg/blob/main/LICENSE
    :alt: MIT License	

Tiny toolbox for time series segmentation.

The toolbox presumes a (univariate or multivariate) time series. For example, consider the following univariate time series:

.. image:: https://raw.githubusercontent.com/RaoulHeese/pytseg/main/docs/source/_static/plot1.png
    :target: https://github.com/RaoulHeese/pytseg/blob/main/docs/source/_static/plot1.png 
    :alt: plot1

Such a time series can then be segmented into distinguishable segments using the toolbox:

.. image:: https://raw.githubusercontent.com/RaoulHeese/pytseg/main/docs/source/_static/plot2.png
    :target: https://github.com/RaoulHeese/pytseg/blob/main/docs/source/_static/plot2.png 
    :alt: plot2

All segments are marked in different colors in the plot. And, finally, these segments can be assigned labels like stationarity:

.. image:: https://raw.githubusercontent.com/RaoulHeese/pytseg/main/docs/source/_static/plot3.png
    :target: https://github.com/RaoulHeese/pytseg/blob/main/docs/source/_static/plot3.png 
    :alt: plot3
   
Green lines indicate stationary segments of the time series.

**Installation**

Install the package via pip or clone this repository. To use pip, type:

.. code-block:: sh

  $ pip install pytseg

**Usage**

Documentation: `<https://pytseg.readthedocs.io/en/latest/>`_.

Demo notebooks can be found in the `demos/` directory of this repository.

📖 **Citation**

If you find this code useful in your research, please consider citing:

.. code-block:: tex

  @misc{pytseg2022,
        author = {Raoul Heese},
        title = {pytseg},
        year = {2022},
        publisher = {GitHub},
        journal = {{GitHub} repository},
        howpublished = {\url{https://github.com/RaoulHeese/pytseg}},
       }

The implemented univariate time series segmentation closely follows:

.. code-block:: tex

  @article{PhysRevE.69.021108,
           title = {Heuristic segmentation of a nonstationary time series},
           author = {Fukuda, Kensuke and Eugene Stanley, H. and Nunes Amaral, Lu\'{\i}s A.},
           journal = {Phys. Rev. E},
           volume = {69},
           issue = {2},
           pages = {021108},
           numpages = {12},
           year = {2004},
           month = {2},
           publisher = {American Physical Society},
           doi = {10.1103/PhysRevE.69.021108},
           url = {https://link.aps.org/doi/10.1103/PhysRevE.69.021108}
          }

There is no affiliation with the authors of this article.
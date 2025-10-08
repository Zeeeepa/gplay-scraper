GPlay Scraper Documentation
===========================

**GPlay Scraper** is a powerful Python Google Play scraper library for extracting comprehensive app data from the Google Play Store. Scrape Google Play Store apps to get ratings, install counts, reviews, ASO metrics, developer information, and 65+ data fields.

.. image:: https://img.shields.io/pypi/v/gplay-scraper.svg
   :target: https://pypi.org/project/gplay-scraper/
   :alt: PyPI Version

.. image:: https://img.shields.io/pypi/pyversions/gplay-scraper.svg
   :target: https://pypi.org/project/gplay-scraper/
   :alt: Python Versions

.. image:: https://img.shields.io/github/license/mohammedcha/gplay-scraper.svg
   :target: https://github.com/mohammedcha/gplay-scraper/blob/main/LICENSE
   :alt: License

Key Features
------------

✅ **Complete Google Play Store data extraction** - 65+ fields per app

✅ **Google Play app analytics** - ratings, installs, reviews, ASO analysis

✅ **Python Google Play scraper** - simple API for developers

✅ **Google Play Store API alternative** - no API keys required

✅ **App store optimization (ASO) tools** - keyword analysis and readability scores

✅ **Bulk Google Play scraping** - analyze multiple apps efficiently

Quick Start
-----------

.. code-block:: python

   from gplay_scraper import GPlayScraper

   # Initialize the scraper
   scraper = GPlayScraper()

   # Get app data
   app_id = "com.hubolabs.hubo"
   title = scraper.get_field(app_id, "title")
   print(f"App Title: {title}")

   # Get multiple fields
   data = scraper.get_fields(app_id, ["title", "score", "installs"])
   
   # Complete analysis
   all_data = scraper.analyze(app_id)

Installation
------------

.. code-block:: bash

   pip install gplay-scraper

Table of Contents
-----------------

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   installation
   quickstart
   api_reference
   examples
   configuration

.. toctree::
   :maxdepth: 2
   :caption: API Reference

   gplay_scraper

.. toctree::
   :maxdepth: 1
   :caption: Additional Information

   changelog
   contributing
   license

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
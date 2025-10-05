Quick Start Guide
=================

This guide will get you up and running with GPlay Scraper in minutes.

Basic Usage
-----------

Import and Initialize
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from gplay_scraper import GPlayScraper
   
   # Initialize the scraper
   scraper = GPlayScraper()

Get Single Field
~~~~~~~~~~~~~~~~

Most efficient for retrieving one piece of data:

.. code-block:: python

   app_id = "com.hubolabs.hubo"
   title = scraper.get_field(app_id, "title")
   print(f"App Title: {title}")
   # Output: App Title: purp - Make new friends

Get Multiple Fields
~~~~~~~~~~~~~~~~~~~

Efficient for several specific fields:

.. code-block:: python

   fields = ["title", "developer", "score", "installs"]
   data = scraper.get_fields(app_id, fields)
   
   for field, value in data.items():
       print(f"{field}: {value}")

Complete Analysis
~~~~~~~~~~~~~~~~~

Get all 65+ available fields:

.. code-block:: python

   all_data = scraper.analyze(app_id)
   print(f"Total fields: {len(all_data)}")
   
   # Access any field
   print(f"Rating: {all_data['score']}")
   print(f"Installs: {all_data['installs']}")

Print Methods
~~~~~~~~~~~~~

For quick debugging and console output:

.. code-block:: python

   # Print single field
   scraper.print_field(app_id, "title")
   
   # Print multiple fields
   scraper.print_fields(app_id, ["title", "score", "developer"])
   
   # Print all data as formatted JSON
   scraper.print_all(app_id)

Finding App Package Names
--------------------------

To use this library, you need the app's package name (app ID):

From Play Store URL
~~~~~~~~~~~~~~~~~~~

.. code-block:: text

   URL: https://play.google.com/store/apps/details?id=com.hubolabs.hubo
   Package name: com.hubolabs.hubo

Common Examples
~~~~~~~~~~~~~~~

- **purp**: ``com.hubolabs.hubo``
- **InterPals**: ``net.interpals``
- **YeeTalk**: ``com.imback.yeetalk``
- **Tellonym**: ``de.tellonym.app``
- **HelloTalk**: ``com.hellotalk``
- **Amino**: ``com.narvii.amino.master``

Available Data Fields
---------------------

The library extracts over 65 different data points about each app. Here's what you can access:

.. note::
   Some fields may return ``None`` if the data is not available for a specific app. This is normal and depends on how the app is configured in the Play Store.

Basic Information
~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 15 35 30

   * - Field
     - Type
     - Description
     - Example
   * - ``appId``
     - string
     - App package name
     - "com.hubolabs.hubo"
   * - ``title``
     - string
     - App title
     - "purp - Make new friends"
   * - ``summary``
     - string
     - Short description
     - "Swipe to make new friends!"
   * - ``description``
     - string
     - Full app description
     - "purp is the best place to make..."
   * - ``appUrl``
     - string
     - Play Store URL
     - "https://play.google.com/store/apps/details?id=com.hubolabs.hubo"

Category & Genre
~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 15 35 30

   * - Field
     - Type
     - Description
     - Example
   * - ``genre``
     - string
     - Primary category
     - "Social"
   * - ``genreId``
     - string
     - Category ID
     - "SOCIAL"
   * - ``categories``
     - list
     - All categories
     - ["Social"]
   * - ``available``
     - boolean
     - App availability
     - true

Ratings & Reviews
~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 15 35 30

   * - Field
     - Type
     - Description
     - Example
   * - ``score``
     - float
     - Average rating (1-5)
     - 4.4
   * - ``ratings``
     - integer
     - Total number of ratings
     - 100175
   * - ``reviews``
     - integer
     - Total number of reviews
     - 5302
   * - ``histogram``
     - list
     - Rating distribution [1★,2★,3★,4★,5★]
     - [8583, 2365, 4440, 7645, 77125]
   * - ``reviewsData``
     - list
     - Recent reviews with user data
     - [{"user": "John", "rating": 4, "text": "Good app!"}]

Install Statistics
~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 15 35 30

   * - Field
     - Type
     - Description
     - Example
   * - ``installs``
     - string
     - Install range
     - "1,000,000+"
   * - ``minInstalls``
     - integer
     - Minimum installs
     - 1000000
   * - ``realInstalls``
     - integer
     - Estimated real installs
     - 4294596
   * - ``dailyInstalls``
     - integer
     - Estimated daily installs
     - 523
   * - ``minDailyInstalls``
     - integer
     - Min daily installs
     - 523
   * - ``realDailyInstalls``
     - integer
     - Real estimated daily installs
     - 2246
   * - ``monthlyInstalls``
     - integer
     - Estimated monthly installs
     - 15920
   * - ``minMonthlyInstalls``
     - integer
     - Min monthly installs
     - 15920
   * - ``realMonthlyInstalls``
     - integer
     - Real estimated monthly installs
     - 68372

Technical Details
~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 15 35 30

   * - Field
     - Type
     - Description
     - Example
   * - ``version``
     - string
     - Current version
     - "4.4.3"
   * - ``androidVersion``
     - integer
     - Required Android version
     - 7
   * - ``maxAndroidApi``
     - integer
     - Maximum API level
     - 34
   * - ``minAndroidApi``
     - integer
     - Minimum API level
     - 26
   * - ``appBundle``
     - string
     - App package name
     - "com.hubolabs.hubo"

Release & Updates
~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 15 35 30

   * - Field
     - Type
     - Description
     - Example
   * - ``released``
     - string
     - Release date
     - "Jul 11, 2020"
   * - ``appAgeDays``
     - integer
     - Age in days
     - 1912
   * - ``lastUpdated``
     - string
     - Last update date
     - "Sep 30, 2025"
   * - ``updatedTimestamp``
     - integer
     - Update timestamp
     - 1759272348
   * - ``whatsNew``
     - list
     - Recent changes
     - ["Bug fixes", "New features"]

Media Content
~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 15 35 30

   * - Field
     - Type
     - Description
     - Example
   * - ``icon``
     - string
     - App icon URL
     - "https://play-lh.googleusercontent.com/..."
   * - ``headerImage``
     - string
     - Header image URL
     - "https://play-lh.googleusercontent.com/..."
   * - ``screenshots``
     - list
     - Screenshot URLs
     - ["https://play-lh.googleusercontent.com/..."]
   * - ``video``
     - string
     - Promo video URL
     - "https://play-lh.googleusercontent.com/..."
   * - ``videoImage``
     - string
     - Video thumbnail URL
     - "https://play-lh.googleusercontent.com/..."

Pricing & Monetization
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 15 35 30

   * - Field
     - Type
     - Description
     - Example
   * - ``price``
     - float
     - App price
     - 0.0
   * - ``currency``
     - string
     - Price currency
     - "USD"
   * - ``free``
     - boolean
     - Is free app
     - true
   * - ``offersIAP``
     - boolean
     - Has in-app purchases
     - true
   * - ``inAppProductPrice``
     - string
     - IAP price range
     - "$0.49 - $29.99 per item"
   * - ``sale``
     - boolean
     - Currently on sale
     - false
   * - ``originalPrice``
     - float
     - Original price if on sale
     - null

Advertising
~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 15 35 30

   * - Field
     - Type
     - Description
     - Example
   * - ``adSupported``
     - boolean
     - Contains ads
     - true
   * - ``containsAds``
     - boolean
     - Shows advertisements
     - true

Content Rating
~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 15 35 30

   * - Field
     - Type
     - Description
     - Example
   * - ``contentRating``
     - string
     - Age rating
     - "Teen"
   * - ``contentRatingDescription``
     - string
     - Rating description
     - "No inappropriate content"

Privacy & Security
~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 15 35 30

   * - Field
     - Type
     - Description
     - Example
   * - ``permissions``
     - object
     - App permissions
     - {"Camera": ["take pictures and videos"]}
   * - ``dataSafety``
     - list
     - Data safety info
     - ["Data is encrypted in transit"]

Developer Information
~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 15 35 30

   * - Field
     - Type
     - Description
     - Example
   * - ``developer``
     - string
     - Developer name
     - "hubo Labs"
   * - ``developerId``
     - string
     - Developer ID
     - "hubo+Labs"
   * - ``developerEmail``
     - string
     - Contact email
     - "support@purp.social"
   * - ``developerWebsite``
     - string
     - Developer website
     - "https://purp.social/"
   * - ``developerAddress``
     - string
     - Developer address
     - "Av. PAULISTA 1636..."
   * - ``developerPhone``
     - string
     - Contact phone
     - "+55 11 98837-3357"
   * - ``privacyPolicy``
     - string
     - Privacy policy URL
     - "https://purp.social/privacy"

ASO (App Store Optimization) Analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 15 35 30

   * - Field
     - Type
     - Description
     - Example
   * - ``totalWords``
     - integer
     - Total words analyzed
     - 152
   * - ``uniqueKeywords``
     - integer
     - Unique keywords found
     - 99
   * - ``topKeywords``
     - object
     - Most frequent keywords
     - {"new": 13, "purp": 12, "friends": 8}
   * - ``topBigrams``
     - object
     - Top 2-word phrases
     - {"make new": 7, "new friends": 7}
   * - ``topTrigrams``
     - object
     - Top 3-word phrases
     - {"make new friends": 7}
   * - ``competitiveKeywords``
     - object
     - Competitive analysis
     - {"social": ["friends", "chat"]}
   * - ``readability``
     - object
     - Text readability score
     - {"flesch_score": 77.38, "flesch_level": "Fairly Easy"}

Next Steps
----------

- Check out :doc:`examples` for real-world use cases
- Read the :doc:`api_reference` for detailed method documentation
- Learn about :doc:`configuration` options
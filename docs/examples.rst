Examples
========

This section provides practical examples for common use cases.

Basic App Information
---------------------

Get essential app details:

.. code-block:: python

   from gplay_scraper import GPlayScraper

   scraper = GPlayScraper()
   app_id = "com.hubolabs.hubo"

   # Get basic info
   basic_info = scraper.get_fields(app_id, [
       "title", "developer", "genre", "score", "free"
   ])

   for field, value in basic_info.items():
       print(f"{field}: {value}")

**Output:**

.. code-block:: text

   title: purp - Make new friends
   developer: hubo Labs
   genre: Social
   score: 4.42
   free: True

Competitive Analysis
--------------------

Compare multiple apps across key metrics:

.. code-block:: python

   from gplay_scraper import GPlayScraper

   scraper = GPlayScraper()

   # Social media apps
   apps = {
       "purp": "com.hubolabs.hubo",
       "InterPals": "net.interpals", 
       "HelloTalk": "com.hellotalk"
   }

   results = []
   for name, app_id in apps.items():
       try:
           data = scraper.get_fields(app_id, [
               "title", "score", "ratings", "installs", "realInstalls"
           ])
           data["name"] = name
           results.append(data)
       except Exception as e:
           print(f"Error analyzing {name}: {e}")

   # Sort by rating
   results.sort(key=lambda x: x.get("score", 0), reverse=True)

   print("Ranking by Rating:")
   for i, app in enumerate(results, 1):
       print(f"{i}. {app['name']}: {app.get('score', 'N/A')} stars")

Install Metrics Analysis
------------------------

Analyze app performance metrics:

.. code-block:: python

   from gplay_scraper import GPlayScraper

   scraper = GPlayScraper()
   app_id = "net.interpals"

   # Get install metrics
   install_metrics = scraper.get_fields(app_id, [
       "installs", "realInstalls", "dailyInstalls", "monthlyInstalls"
   ])

   print("Install Performance:")
   for metric, value in install_metrics.items():
       if isinstance(value, int):
           print(f"  {metric}: {value:,}")
       else:
           print(f"  {metric}: {value}")

ASO Keyword Analysis
--------------------

Analyze keywords for App Store Optimization:

.. code-block:: python

   from gplay_scraper import GPlayScraper

   scraper = GPlayScraper()
   app_id = "com.imback.yeetalk"

   # Get ASO data
   aso_data = scraper.get_fields(app_id, [
       "topKeywords", "uniqueKeywords", "competitiveKeywords", "readability"
   ])

   print("ASO Analysis:")
   print(f"  Unique Keywords: {aso_data['uniqueKeywords']}")
   print(f"  Top Keywords: {list(aso_data['topKeywords'].keys())[:5]}")
   print(f"  Readability: {aso_data['readability']['flesch_level']}")

Batch Processing
----------------

Analyze multiple apps efficiently:

.. code-block:: python

   from gplay_scraper import GPlayScraper

   scraper = GPlayScraper()

   # Apps to analyze
   apps_to_analyze = [
       "com.hubolabs.hubo",
       "net.interpals",
       "com.hellotalk",
       "de.tellonym.app"
   ]

   results = []
   for app_id in apps_to_analyze:
       try:
           data = scraper.get_fields(app_id, [
               "title", "score", "ratings", "installs", "developer"
           ])
           results.append(data)
           print(f"✓ Analyzed {data['title']}")
       except Exception as e:
           print(f"✗ Error analyzing {app_id}: {e}")

   # Sort by rating
   results.sort(key=lambda x: x['score'], reverse=True)
   
   print("\nTop Rated Apps:")
   for app in results:
       print(f"{app['title']}: {app['score']} stars")

Complete App Report
-------------------

Generate a comprehensive app analysis report:

.. code-block:: python

   from gplay_scraper import GPlayScraper

   def generate_app_report(app_id):
       scraper = GPlayScraper()
       data = scraper.analyze(app_id)
       
       print(f"=== {data['title']} ===")
       print(f"Developer: {data['developer']}")
       print(f"Category: {data['genre']}")
       print(f"Rating: {data['score']} ({data['ratings']:,} ratings)")
       print(f"Installs: {data['installs']}")
       
       price_text = 'Free' if data['free'] else f"${data['price']}"
       print(f"Price: {price_text}")
       print(f"Last Updated: {data['lastUpdated']}")
       print(f"App Age: {data['appAgeDays']} days")
       
       # ASO insights
       print(f"\nASO Insights:")
       print(f"  Keywords: {data['uniqueKeywords']}")
       print(f"  Readability: {data['readability']['flesch_level']}")

   # Generate report
   generate_app_report("com.narvii.amino.master")

Error Handling
--------------

Handle errors gracefully:

.. code-block:: python

   from gplay_scraper import GPlayScraper

   scraper = GPlayScraper()

   def safe_analyze(app_id):
       try:
           data = scraper.get_fields(app_id, ["title", "score", "installs"])
           return data
       except ValueError as e:
           print(f"Invalid app ID: {e}")
           return None
       except Exception as e:
           print(f"Unexpected error: {e}")
           return None

   # Test with valid app ID
   result = safe_analyze("com.hubolabs.hubo")
   if result:
       print("Analysis successful!")
   else:
       print("Analysis failed.")

Configuration Examples
----------------------

Customize scraper behavior:

.. code-block:: python

   from gplay_scraper import GPlayScraper, Config

   # View default settings
   print(f"Default timeout: {Config.DEFAULT_TIMEOUT}s")
   print(f"Default rate limit: {Config.RATE_LIMIT_DELAY}s")

   # Create scraper with custom rate limiting
   scraper = GPlayScraper()
   scraper.scraper.rate_limit_delay = 2.0  # 2 seconds between requests

   # Use custom configuration
   headers = Config.get_headers("Custom User Agent")
   print(f"Custom headers: {headers}")

Real-World Use Cases
--------------------

**Market Research**
  Analyze competitor apps to understand market positioning and user satisfaction.

**ASO Optimization**
  Extract keywords and readability scores to optimize your app's store listing.

**App Monitoring**
  Track your app's performance metrics over time.

**Data Analysis**
  Collect app data for research, reporting, or machine learning projects.

**Competitive Intelligence**
  Monitor competitor updates, ratings, and user feedback.
# App Methods

Extract detailed information about individual Google Play Store apps.

## Quick Start

```python
from gplay_scraper import GPlayScraper

scraper = GPlayScraper()

# Get all data
data = scraper.app_analyze("com.whatsapp")
print(data['title'], data['score'], data['installs'])

# Get specific fields
title = scraper.app_get_field("com.whatsapp", "title")
print(title)  # WhatsApp Messenger

# Get multiple fields
info = scraper.app_get_fields("com.whatsapp", ["title", "score", "developer"])
print(info)
```

---

## HTTP Clients

The library supports 7 HTTP clients with automatic fallback. If one fails, it tries the next.

### Supported Clients
1. **requests** (default) - Standard Python HTTP library
2. **curl_cffi** - cURL with browser impersonation
3. **tls_client** - Advanced TLS fingerprinting
4. **httpx** - Modern async-capable HTTP client
5. **urllib3** - Low-level HTTP client
6. **cloudscraper** - Cloudflare bypass
7. **aiohttp** - Async HTTP client

### Usage

```python
# Default (tries requests first, then others)
scraper = GPlayScraper()

# Specify a client
scraper = GPlayScraper(http_client="curl_cffi")
scraper = GPlayScraper(http_client="tls_client")
scraper = GPlayScraper(http_client="httpx")
```

### Installation

```bash
# Default
pip install requests

# Advanced clients (optional)
pip install curl-cffi
pip install tls-client
pip install httpx
pip install urllib3
pip install cloudscraper
pip install aiohttp
```

**Note:** The library automatically falls back to available clients if your preferred one fails.

---

## Methods

### `app_analyze(app_id, lang='en', country='us')`
Returns all 65+ fields as a dictionary.

```python
data = scraper.app_analyze("com.whatsapp")
# Returns: {'appId': 'com.whatsapp', 'title': 'WhatsApp Messenger', ...}
```

### `app_get_field(app_id, field, lang='en', country='us')`
Returns a single field value.

```python
score = scraper.app_get_field("com.whatsapp", "score")
# Returns: 4.2
```

### `app_get_fields(app_id, fields, lang='en', country='us')`
Returns multiple fields as a dictionary.

```python
data = scraper.app_get_fields("com.whatsapp", ["title", "score", "installs"])
# Returns: {'title': 'WhatsApp Messenger', 'score': 4.2, 'installs': '5,000,000,000+'}
```

### `app_print_field(app_id, field, lang='en', country='us')`
Prints a single field to console.

```python
scraper.app_print_field("com.whatsapp", "title")
# Output: title: WhatsApp Messenger
```

### `app_print_fields(app_id, fields, lang='en', country='us')`
Prints multiple fields to console.

```python
scraper.app_print_fields("com.whatsapp", ["title", "score"])
# Output:
# title: WhatsApp Messenger
# score: 4.2
```

### `app_print_all(app_id, lang='en', country='us')`
Prints all fields as formatted JSON.

```python
scraper.app_print_all("com.whatsapp")
# Output: Full JSON with all 65+ fields
```

---

## Available Fields (65+)

### Basic Information
- `appId` - Package name (e.g., "com.whatsapp")
- `title` - App name
- `summary` - Short description
- `description` - Full description
- `appUrl` - Play Store URL

### Ratings & Reviews
- `score` - Average rating (1-5)
- `ratings` - Total number of ratings
- `reviews` - Total number of reviews
- `histogram` - Rating distribution [1★, 2★, 3★, 4★, 5★]

### Install Metrics
- `installs` - Install range (e.g., "10,000,000+")
- `minInstalls` - Minimum installs
- `realInstalls` - Estimated real installs
- `dailyInstalls` - Estimated daily installs
- `monthlyInstalls` - Estimated monthly installs
- `minDailyInstalls` - Minimum daily installs
- `realDailyInstalls` - Real estimated daily installs
- `minMonthlyInstalls` - Minimum monthly installs
- `realMonthlyInstalls` - Real estimated monthly installs

### Pricing
- `price` - Price in currency (0 if free)
- `currency` - Currency code (e.g., "USD")
- `free` - Boolean, true if free
- `offersIAP` - Has in-app purchases
- `inAppProductPrice` - IAP price range
- `sale` - Currently on sale
- `originalPrice` - Original price if on sale

### Media
- `icon` - App icon URL
- `headerImage` - Header image URL
- `screenshots` - List of screenshot URLs
- `video` - Promo video URL
- `videoImage` - Video thumbnail URL

### Developer
- `developer` - Developer name
- `developerId` - Developer ID
- `developerEmail` - Contact email
- `developerWebsite` - Website URL
- `developerAddress` - Physical address
- `developerPhone` - Contact phone
- `privacyPolicy` - Privacy policy URL

### Category
- `genre` - Primary category (e.g., "Communication")
- `genreId` - Category ID (e.g., "COMMUNICATION")
- `categories` - List of categories

### Technical
- `version` - Current version
- `androidVersion` - Required Android version
- `minAndroidApi` - Minimum API level
- `maxAndroidApi` - Maximum API level
- `appBundle` - App bundle name

### Dates
- `released` - Release date (e.g., "Feb 24, 2009")
- `appAgeDays` - Age in days
- `lastUpdated` - Last update date
- `updatedTimestamp` - Update timestamp

### Content
- `contentRating` - Age rating (e.g., "Everyone")
- `contentRatingDescription` - Rating description
- `whatsNew` - Recent changes list
- `permissions` - Required permissions dict
- `dataSafety` - Data safety info list

### Advertising
- `adSupported` - Contains ads
- `containsAds` - Shows advertisements

### Availability
- `available` - App is available

---

## Practical Examples

### Competitive Analysis
```python
apps = ["com.whatsapp", "com.telegram", "com.viber"]
for app_id in apps:
    data = scraper.app_get_fields(app_id, ["title", "score", "realInstalls"])
    print(f"{data['title']}: {data['score']}★ - {data['realInstalls']:,} installs")
```

### Monitor App Updates
```python
app_id = "com.whatsapp"
data = scraper.app_get_fields(app_id, ["version", "lastUpdated", "whatsNew"])
print(f"Version: {data['version']}")
print(f"Updated: {data['lastUpdated']}")
print(f"Changes: {data['whatsNew']}")
```

### Extract Developer Info
```python
app_id = "com.whatsapp"
dev_info = scraper.app_get_fields(app_id, [
    "developer", "developerEmail", "developerWebsite"
])
print(dev_info)
```

### Check Monetization
```python
app_id = "com.whatsapp"
money = scraper.app_get_fields(app_id, [
    "free", "price", "offersIAP", "containsAds"
])
print(f"Free: {money['free']}")
print(f"Has IAP: {money['offersIAP']}")
print(f"Has Ads: {money['containsAds']}")
```

---

## Parameters

### Initialization
- `http_client` (str, optional) - HTTP client to use: "requests", "curl_cffi", "tls_client", "httpx", "urllib3", "cloudscraper", "aiohttp" (default: "requests")

### Method Parameters
- `app_id` (str, required) - App package name from Play Store URL
- `lang` (str, optional) - Language code (default: 'en')
- `country` (str, optional) - Country code (default: 'us')
- `field` (str) - Single field name
- `fields` (List[str]) - List of field names

### Finding App IDs
From Play Store URL: `https://play.google.com/store/apps/details?id=com.whatsapp`  
The app_id is: `com.whatsapp`

### Language & Country Codes
- **Language**: 'en', 'es', 'fr', 'de', 'ja', 'ko', 'pt', 'ru', 'zh', etc.
- **Country**: 'us', 'gb', 'ca', 'au', 'in', 'br', 'jp', 'kr', 'de', 'fr', etc.

---

## When to Use Each Method

- **`app_analyze()`** - Need all data for comprehensive analysis
- **`app_get_field()`** - Need just one specific value
- **`app_get_fields()`** - Need several specific fields (more efficient than multiple get_field calls)
- **`app_print_field()`** - Quick debugging/console output
- **`app_print_fields()`** - Quick debugging of multiple values
- **`app_print_all()`** - Explore available data structure

---

## Advanced Features

### Rate Limiting
Built-in rate limiting (1 second delay between requests) prevents blocking.

### Error Handling
```python
from gplay_scraper import GPlayScraper, AppNotFoundError, NetworkError

scraper = GPlayScraper()

try:
    data = scraper.app_analyze("invalid.app.id")
except AppNotFoundError:
    print("App not found")
except NetworkError:
    print("Network error occurred")
```

### Multi-Region Data
```python
# Get data from different regions
us_data = scraper.app_analyze("com.whatsapp", country="us")
uk_data = scraper.app_analyze("com.whatsapp", country="gb")
jp_data = scraper.app_analyze("com.whatsapp", country="jp", lang="ja")
```

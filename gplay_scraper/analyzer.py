import json
from typing import Any, List, Dict
from datetime import datetime, timezone
import logging

from .core.scraper import PlayStoreScraper
from .core.aso_analyzer import AsoAnalyzer
from .models.element_specs import ElementSpecs
from .utils.helpers import (
    calculate_app_age, calculate_daily_installs, calculate_monthly_installs, clean_json_string
)

# Configure logging only if not already configured
if not logging.getLogger().handlers:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class GPlayScraper:
    """Main Google Play Store scraper class.
    
    Provides methods to extract comprehensive app data from Google Play Store
    including ratings, installs, reviews, ASO metrics, and 65+ data fields.
    
    Example:
        >>> scraper = GPlayScraper()
        >>> data = scraper.analyze("com.hubolabs.hubo")
        >>> title = scraper.get_field("com.hubolabs.hubo", "title")
    """
    
    def __init__(self):
        """Initialize the scraper with required components."""
        self.scraper = PlayStoreScraper()
        self.aso_analyzer = AsoAnalyzer()
        self._cache = {}  # Cache for analyzed app data

    def analyze(self, app_id: str) -> Dict:
        """Analyze a Google Play Store app and return all available data.
        
        Args:
            app_id (str): The app's package name (e.g., "com.hubolabs.hubo")
            
        Returns:
            Dict: Complete app data with 65+ fields including ratings, installs,
                 reviews, ASO metrics, developer info, and technical details
                 
        Raises:
            ValueError: If app_id is invalid or empty
            Exception: If scraping or parsing fails
            
        Example:
            >>> scraper = GPlayScraper()
            >>> data = scraper.analyze("com.hubolabs.hubo")
            >>> print(f"App: {data['title']}, Rating: {data['score']}")
        """
        # Validate input parameters
        if not app_id or not isinstance(app_id, str):
            raise ValueError("app_id must be a non-empty string")
            
        try:
            # Scrape raw data from Google Play Store
            ds5_data, ds11_data = self.scraper.scrape_play_store_data(app_id)
        except Exception as e:
            logger.error(f"Failed to scrape data for {app_id}: {e}")
            raise

        # Clean and parse JSON data
        json_str_cleaned = clean_json_string(ds5_data)
        try:
            data = json.loads(json_str_cleaned)
        except json.JSONDecodeError as e:
            logger.error(f"JSON parsing error for ds:5: {e}")
            logger.debug(f"Cleaned JSON string causing error: {json_str_cleaned[:200]}")
            raise ValueError(f"Failed to parse ds:5 JSON: {str(e)}")

        # Extract app details using element specifications
        app_details = {}
        for key, spec in ElementSpecs.Detail.items():
            app_details[key] = spec.extract_content(data)

        # Add computed fields
        app_details['appId'] = app_id
        app_details['url'] = f"https://play.google.com/store/apps/details?id={app_id}"

        # Calculate time-based metrics if release date is available
        current_date = datetime.now(timezone.utc)
        release_date_str = app_details.get("released")
        if release_date_str:
            # Calculate app age and install metrics
            app_details["appAge"] = calculate_app_age(release_date_str, current_date)
            app_details["dailyInstalls"] = calculate_daily_installs(app_details.get("installs"), release_date_str, current_date)
            app_details["minDailyInstalls"] = calculate_daily_installs(app_details.get("minInstalls"), release_date_str, current_date)
            app_details["realDailyInstalls"] = calculate_daily_installs(app_details.get("realInstalls"), release_date_str, current_date)
            app_details["monthlyInstalls"] = calculate_monthly_installs(app_details.get("installs"), release_date_str, current_date)
            app_details["minMonthlyInstalls"] = calculate_monthly_installs(app_details.get("minInstalls"), release_date_str, current_date)
            app_details["realMonthlyInstalls"] = calculate_monthly_installs(app_details.get("realInstalls"), release_date_str, current_date)
        else:
            # Set metrics to None if no release date available
            metric_keys = [
                "appAge", "dailyInstalls", "minDailyInstalls", "realDailyInstalls",
                "monthlyInstalls", "minMonthlyInstalls", "realMonthlyInstalls"
            ]
            for key in metric_keys:
                app_details[key] = None

        # Perform ASO analysis and extract reviews
        app_details['keywordAnalysis'] = self.aso_analyzer.analyze_app_text(app_details)
        app_details['reviewsData'] = self.scraper.extract_reviews(ds11_data)

        return self._format_app_details(app_details)

    def _format_app_details(self, details: dict) -> dict:
        """Format and structure app details into final output format.
        
        Args:
            details (dict): Raw app details from scraping and analysis
            
        Returns:
            dict: Formatted app data with standardized field names
        """
        keyword_analysis = details.get("keywordAnalysis", {})
        
        # Map internal field names to public API field names
        field_mapping = {
            "appId": "appId", "title": "title", "summary": "summary", "description": "description",
            "appUrl": "url", "genre": "genre", "genreId": "genreId", "categories": "categories",
            "available": "available", "released": "released", "appAgeDays": "appAge",
            "lastUpdated": "lastUpdatedOn", "updatedTimestamp": "updated", "icon": "icon",
            "headerImage": "headerImage", "screenshots": "screenshots", "video": "video",
            "videoImage": "videoImage", "installs": "installs", "minInstalls": "minInstalls",
            "realInstalls": "realInstalls", "dailyInstalls": "dailyInstalls",
            "minDailyInstalls": "minDailyInstalls", "realDailyInstalls": "realDailyInstalls",
            "monthlyInstalls": "monthlyInstalls", "minMonthlyInstalls": "minMonthlyInstalls",
            "realMonthlyInstalls": "realMonthlyInstalls", "score": "score", "ratings": "ratings",
            "reviews": "reviews", "histogram": "histogram", "reviewsData": "reviewsData",
            "adSupported": "adSupported", "containsAds": "containsAds", "version": "version",
            "androidVersion": "androidVersion", "maxAndroidApi": "maxandroidapi",
            "minAndroidApi": "minandroidapi", "appBundle": "appBundle",
            "contentRating": "contentRating", "contentRatingDescription": "contentRatingDescription",
            "whatsNew": "whatsNew", "permissions": "permissions", "dataSafety": "dataSafety",
            "price": "price", "currency": "currency", "free": "free", "offersIAP": "offersIAP",
            "inAppProductPrice": "inAppProductPrice", "sale": "sale", "originalPrice": "originalPrice",
            "developer": "developer", "developerId": "developerId", "developerEmail": "developerEmail",
            "developerWebsite": "developerWebsite", "developerAddress": "developerAddress",
            "developerPhone": "developerPhone", "privacyPolicy": "privacyPolicy"
        }
        
        # Build result dictionary with mapped field names
        result = {out_key: details.get(in_key) for out_key, in_key in field_mapping.items()}
        
        # Add ASO keyword analysis fields
        keyword_fields = {
            "totalWords": "total_words", "uniqueKeywords": "unique_keywords",
            "topKeywords": "top_keywords", "topBigrams": "top_bigrams",
            "topTrigrams": "top_trigrams", "competitiveKeywords": "competitive_analysis",
            "readability": "readability"
        }
        result.update({out_key: keyword_analysis.get(in_key) for out_key, in_key in keyword_fields.items()})
        
        return result

    def _get_cached_data(self, app_id: str) -> Dict:
        """Get cached app data or analyze if not cached.
        
        Args:
            app_id (str): App package name
            
        Returns:
            Dict: Complete app analysis data
        """
        if app_id not in self._cache:
            self._cache[app_id] = self.analyze(app_id)
        return self._cache[app_id]

    def get_field(self, app_id: str, field: str) -> Any:
        """Get a specific field value from app analysis.
        
        Args:
            app_id (str): App package name (e.g., "com.hubolabs.hubo")
            field (str): Field name to retrieve (e.g., "title", "score")
            
        Returns:
            Any: Field value or None if not found
            
        Example:
            >>> scraper = GPlayScraper()
            >>> title = scraper.get_field("com.hubolabs.hubo", "title")
        """
        return self._get_cached_data(app_id).get(field)

    def get_fields(self, app_id: str, fields: List[str]) -> Dict[str, Any]:
        """Get multiple specific fields from app analysis.
        
        Args:
            app_id (str): App package name
            fields (List[str]): List of field names to retrieve
            
        Returns:
            Dict[str, Any]: Dictionary with requested fields and values
            
        Example:
            >>> scraper = GPlayScraper()
            >>> data = scraper.get_fields("com.hubolabs.hubo", ["title", "score", "installs"])
        """
        data = self._get_cached_data(app_id)
        return {field: data.get(field) for field in fields}

    def print_field(self, app_id: str, field: str) -> None:
        """Print a specific field value to console.
        
        Args:
            app_id (str): App package name
            field (str): Field name to print
            
        Example:
            >>> scraper = GPlayScraper()
            >>> scraper.print_field("com.hubolabs.hubo", "title")
            title: purp - Make new friends
        """
        value = self.get_field(app_id, field)
        try:
            print(f"{field}: {value}")
        except UnicodeEncodeError:
            # Handle Unicode characters that can't be displayed
            print(f"{field}: {repr(value)}")

    def print_fields(self, app_id: str, fields: List[str]) -> None:
        """Print multiple field values to console.
        
        Args:
            app_id (str): App package name
            fields (List[str]): List of field names to print
            
        Example:
            >>> scraper = GPlayScraper()
            >>> scraper.print_fields("com.hubolabs.hubo", ["title", "score", "developer"])
        """
        data = self.get_fields(app_id, fields)
        for field, value in data.items():
            try:
                print(f"{field}: {value}")
            except UnicodeEncodeError:
                # Handle Unicode characters that can't be displayed
                print(f"{field}: {repr(value)}")

    def print_all(self, app_id: str) -> None:
        """Print all app data as formatted JSON.
        
        Args:
            app_id (str): App package name
            
        Example:
            >>> scraper = GPlayScraper()
            >>> scraper.print_all("com.hubolabs.hubo")
            # Outputs complete JSON with all 65+ fields
        """
        data = self._get_cached_data(app_id)
        try:
            # Print with Unicode support
            print(json.dumps(data, indent=2, ensure_ascii=False))
        except UnicodeEncodeError:
            # Fallback to ASCII-safe output
            print(json.dumps(data, indent=2, ensure_ascii=True))
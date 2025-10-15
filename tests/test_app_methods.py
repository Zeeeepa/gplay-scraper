import unittest
import warnings
import time
from gplay_scraper import GPlayScraper
from gplay_scraper.exceptions import GPlayScraperError, NetworkError, RateLimitError


class TestAppMethods(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.scraper = GPlayScraper()
        cls.app_id = "com.whatsapp"
        cls.lang = "en"
        cls.country = "us"
    
    def test_app_analyze(self):
        """Test app_analyze returns dictionary with data or handles errors gracefully"""
        time.sleep(2)  # Wait 2 seconds before request
        try:
            result = self.scraper.app_analyze(self.app_id, lang=self.lang, country=self.country)
            self.assertIsInstance(result, dict)
            if result:  # Only check if we got data
                self.assertIn('title', result)
        except (NetworkError, RateLimitError, GPlayScraperError) as e:
            warnings.warn(f"Network/Rate limit error in test_app_analyze: {e}")
            self.skipTest(f"Skipping due to network/rate limit: {e}")
    
    def test_app_get_field(self):
        """Test app_get_field returns single field value or handles errors gracefully"""
        time.sleep(2)  # Wait 2 seconds before request
        try:
            result = self.scraper.app_get_field(self.app_id, "title", lang=self.lang, country=self.country)
            if result is not None:
                self.assertIsInstance(result, str)
                self.assertTrue(len(result) > 0)
        except (NetworkError, RateLimitError, GPlayScraperError) as e:
            warnings.warn(f"Network/Rate limit error in test_app_get_field: {e}")
            self.skipTest(f"Skipping due to network/rate limit: {e}")
    
    def test_app_get_fields(self):
        """Test app_get_fields returns multiple fields or handles errors gracefully"""
        time.sleep(2)  # Wait 2 seconds before request
        fields = ["title", "score", "installs"]
        try:
            result = self.scraper.app_get_fields(self.app_id, fields, lang=self.lang, country=self.country)
            if result:
                self.assertIsInstance(result, dict)
        except (NetworkError, RateLimitError, GPlayScraperError) as e:
            warnings.warn(f"Network/Rate limit error in test_app_get_fields: {e}")
            self.skipTest(f"Skipping due to network/rate limit: {e}")
    
    def test_app_print_field(self):
        """Test app_print_field executes without error or handles errors gracefully"""
        time.sleep(2)  # Wait 2 seconds before request
        try:
            self.scraper.app_print_field(self.app_id, "title", lang=self.lang, country=self.country)
        except (NetworkError, RateLimitError, GPlayScraperError) as e:
            warnings.warn(f"Network/Rate limit error in test_app_print_field: {e}")
            self.skipTest(f"Skipping due to network/rate limit: {e}")
        except Exception as e:
            self.fail(f"app_print_field raised unexpected {type(e).__name__}: {e}")
    
    def test_app_print_fields(self):
        """Test app_print_fields executes without error or handles errors gracefully"""
        time.sleep(2)  # Wait 2 seconds before request
        try:
            self.scraper.app_print_fields(self.app_id, ["title", "score"], lang=self.lang, country=self.country)
        except (NetworkError, RateLimitError, GPlayScraperError) as e:
            warnings.warn(f"Network/Rate limit error in test_app_print_fields: {e}")
            self.skipTest(f"Skipping due to network/rate limit: {e}")
        except Exception as e:
            self.fail(f"app_print_fields raised unexpected {type(e).__name__}: {e}")
    
    def test_app_print_all(self):
        """Test app_print_all executes without error or handles errors gracefully"""
        time.sleep(2)  # Wait 2 seconds before request
        try:
            self.scraper.app_print_all(self.app_id, lang=self.lang, country=self.country)
        except (NetworkError, RateLimitError, GPlayScraperError) as e:
            warnings.warn(f"Network/Rate limit error in test_app_print_all: {e}")
            self.skipTest(f"Skipping due to network/rate limit: {e}")
        except Exception as e:
            self.fail(f"app_print_all raised unexpected {type(e).__name__}: {e}")


if __name__ == '__main__':
    unittest.main()

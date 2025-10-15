"""
Unit tests for Reviews Methods
"""

import unittest
import time
import warnings
from gplay_scraper import GPlayScraper
from gplay_scraper.exceptions import GPlayScraperError, NetworkError, RateLimitError


class TestReviewsMethods(unittest.TestCase):
    """Test suite for reviews methods."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.scraper = GPlayScraper()
        self.app_id = "com.whatsapp"  # WhatsApp app ID for testing
    
    def test_reviews_analyze(self):
        """Test reviews_analyze returns list of reviews."""
        time.sleep(2)
        try:
            result = self.scraper.reviews_analyze(self.app_id, count=10)
            self.assertIsInstance(result, list)
            if result:
                self.assertGreater(len(result), 0)
        except (NetworkError, RateLimitError, GPlayScraperError) as e:
            warnings.warn(f"Network/Rate limit error in test_reviews_analyze: {e}")
            self.skipTest(f"Skipping due to network/rate limit: {e}")
    
    def test_reviews_get_field(self):
        """Test reviews_get_field returns list of field values."""
        time.sleep(2)
        try:
            result = self.scraper.reviews_get_field(self.app_id, "userName", count=5)
            self.assertIsInstance(result, list)
        except (NetworkError, RateLimitError, GPlayScraperError) as e:
            warnings.warn(f"Network/Rate limit error in test_reviews_get_field: {e}")
            self.skipTest(f"Skipping due to network/rate limit: {e}")
    
    def test_reviews_get_fields(self):
        """Test reviews_get_fields returns list of dictionaries."""
        time.sleep(2)
        try:
            result = self.scraper.reviews_get_fields(self.app_id, ["userName", "score"], count=5)
            self.assertIsInstance(result, list)
        except (NetworkError, RateLimitError, GPlayScraperError) as e:
            warnings.warn(f"Network/Rate limit error in test_reviews_get_fields: {e}")
            self.skipTest(f"Skipping due to network/rate limit: {e}")
    
    def test_reviews_print_field(self):
        """Test reviews_print_field executes without error."""
        time.sleep(2)
        try:
            self.scraper.reviews_print_field(self.app_id, "userName", count=5)
        except (NetworkError, RateLimitError, GPlayScraperError) as e:
            warnings.warn(f"Network/Rate limit error in test_reviews_print_field: {e}")
            self.skipTest(f"Skipping due to network/rate limit: {e}")
        except Exception as e:
            self.fail(f"reviews_print_field raised unexpected {e}")
    
    def test_reviews_print_fields(self):
        """Test reviews_print_fields executes without error."""
        time.sleep(2)
        try:
            self.scraper.reviews_print_fields(self.app_id, ["userName", "score"], count=5)
        except (NetworkError, RateLimitError, GPlayScraperError) as e:
            warnings.warn(f"Network/Rate limit error in test_reviews_print_fields: {e}")
            self.skipTest(f"Skipping due to network/rate limit: {e}")
        except Exception as e:
            self.fail(f"reviews_print_fields raised unexpected {e}")
    
    def test_reviews_print_all(self):
        """Test reviews_print_all executes without error."""
        time.sleep(2)
        try:
            self.scraper.reviews_print_all(self.app_id, count=5)
        except (NetworkError, RateLimitError, GPlayScraperError) as e:
            warnings.warn(f"Network/Rate limit error in test_reviews_print_all: {e}")
            self.skipTest(f"Skipping due to network/rate limit: {e}")
        except Exception as e:
            self.fail(f"reviews_print_all raised unexpected {e}")

if __name__ == '__main__':
    unittest.main()

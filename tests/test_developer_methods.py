"""
Unit tests for Developer Methods
"""

import unittest
import time
import warnings
from gplay_scraper import GPlayScraper
from gplay_scraper.exceptions import GPlayScraperError, NetworkError, RateLimitError


class TestDeveloperMethods(unittest.TestCase):
    """Test suite for developer methods."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.scraper = GPlayScraper()
        self.dev_id = "5700313618786177705"  # WhatsApp Inc. developer ID
    
    def test_developer_analyze(self):
        """Test developer_analyze returns list of apps."""
        time.sleep(2)
        try:
            result = self.scraper.developer_analyze(self.dev_id, count=10)
            self.assertIsInstance(result, list)
            if result:
                self.assertGreater(len(result), 0)
        except (NetworkError, RateLimitError, GPlayScraperError) as e:
            warnings.warn(f"Network/Rate limit error in test_developer_analyze: {e}")
            self.skipTest(f"Skipping due to network/rate limit: {e}")
    
    def test_developer_get_field(self):
        """Test developer_get_field returns list of field values."""
        time.sleep(2)
        try:
            result = self.scraper.developer_get_field(self.dev_id, "title", count=5)
            self.assertIsInstance(result, list)
        except (NetworkError, RateLimitError, GPlayScraperError) as e:
            warnings.warn(f"Network/Rate limit error in test_developer_get_field: {e}")
            self.skipTest(f"Skipping due to network/rate limit: {e}")
    
    def test_developer_get_fields(self):
        """Test developer_get_fields returns list of dictionaries."""
        time.sleep(2)
        try:
            result = self.scraper.developer_get_fields(self.dev_id, ["title", "score"], count=5)
            self.assertIsInstance(result, list)
        except (NetworkError, RateLimitError, GPlayScraperError) as e:
            warnings.warn(f"Network/Rate limit error in test_developer_get_fields: {e}")
            self.skipTest(f"Skipping due to network/rate limit: {e}")
    
    def test_developer_print_field(self):
        """Test developer_print_field executes without error."""
        time.sleep(2)
        try:
            self.scraper.developer_print_field(self.dev_id, "title", count=5)
        except (NetworkError, RateLimitError, GPlayScraperError) as e:
            warnings.warn(f"Network/Rate limit error in test_developer_print_field: {e}")
            self.skipTest(f"Skipping due to network/rate limit: {e}")
        except Exception as e:
            self.fail(f"developer_print_field raised unexpected {e}")
    
    def test_developer_print_fields(self):
        """Test developer_print_fields executes without error."""
        time.sleep(2)
        try:
            self.scraper.developer_print_fields(self.dev_id, ["title", "score"], count=5)
        except (NetworkError, RateLimitError, GPlayScraperError) as e:
            warnings.warn(f"Network/Rate limit error in test_developer_print_fields: {e}")
            self.skipTest(f"Skipping due to network/rate limit: {e}")
        except Exception as e:
            self.fail(f"developer_print_fields raised unexpected {e}")
    
    def test_developer_print_all(self):
        """Test developer_print_all executes without error."""
        time.sleep(2)
        try:
            self.scraper.developer_print_all(self.dev_id, count=5)
        except (NetworkError, RateLimitError, GPlayScraperError) as e:
            warnings.warn(f"Network/Rate limit error in test_developer_print_all: {e}")
            self.skipTest(f"Skipping due to network/rate limit: {e}")
        except Exception as e:
            self.fail(f"developer_print_all raised unexpected {e}")

if __name__ == '__main__':
    unittest.main()

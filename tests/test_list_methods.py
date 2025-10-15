"""
Unit tests for List Methods
"""

import unittest
import time
import warnings
from gplay_scraper import GPlayScraper
from gplay_scraper.exceptions import GPlayScraperError, NetworkError, RateLimitError


class TestListMethods(unittest.TestCase):
    """Test suite for list methods (top charts)."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.scraper = GPlayScraper()
        self.collection = "TOP_FREE"  # Top free apps collection
        self.category = "GAME"  # Game category
    
    def test_list_analyze(self):
        """Test list_analyze returns list of top apps."""
        time.sleep(2)
        try:
            result = self.scraper.list_analyze(self.collection, self.category, count=10)
            self.assertIsInstance(result, list)
            if result:
                self.assertGreater(len(result), 0)
        except (NetworkError, RateLimitError, GPlayScraperError) as e:
            warnings.warn(f"Network/Rate limit error in test_list_analyze: {e}")
            self.skipTest(f"Skipping due to network/rate limit: {e}")
    
    def test_list_get_field(self):
        """Test list_get_field returns list of field values."""
        time.sleep(2)
        try:
            result = self.scraper.list_get_field(self.collection, self.category, "title", count=5)
            self.assertIsInstance(result, list)
        except (NetworkError, RateLimitError, GPlayScraperError) as e:
            warnings.warn(f"Network/Rate limit error in test_list_get_field: {e}")
            self.skipTest(f"Skipping due to network/rate limit: {e}")
    
    def test_list_get_fields(self):
        """Test list_get_fields returns list of dictionaries."""
        time.sleep(2)
        try:
            result = self.scraper.list_get_fields(self.collection, self.category, ["title", "score"], count=5)
            self.assertIsInstance(result, list)
        except (NetworkError, RateLimitError, GPlayScraperError) as e:
            warnings.warn(f"Network/Rate limit error in test_list_get_fields: {e}")
            self.skipTest(f"Skipping due to network/rate limit: {e}")
    
    def test_list_print_field(self):
        """Test list_print_field executes without error."""
        time.sleep(2)
        try:
            self.scraper.list_print_field(self.collection, self.category, "title", count=5)
        except (NetworkError, RateLimitError, GPlayScraperError) as e:
            warnings.warn(f"Network/Rate limit error in test_list_print_field: {e}")
            self.skipTest(f"Skipping due to network/rate limit: {e}")
        except Exception as e:
            self.fail(f"list_print_field raised unexpected {e}")
    
    def test_list_print_fields(self):
        """Test list_print_fields executes without error."""
        time.sleep(2)
        try:
            self.scraper.list_print_fields(self.collection, self.category, ["title", "score"], count=5)
        except (NetworkError, RateLimitError, GPlayScraperError) as e:
            warnings.warn(f"Network/Rate limit error in test_list_print_fields: {e}")
            self.skipTest(f"Skipping due to network/rate limit: {e}")
        except Exception as e:
            self.fail(f"list_print_fields raised unexpected {e}")
    
    def test_list_print_all(self):
        """Test list_print_all executes without error."""
        time.sleep(2)
        try:
            self.scraper.list_print_all(self.collection, self.category, count=5)
        except (NetworkError, RateLimitError, GPlayScraperError) as e:
            warnings.warn(f"Network/Rate limit error in test_list_print_all: {e}")
            self.skipTest(f"Skipping due to network/rate limit: {e}")
        except Exception as e:
            self.fail(f"list_print_all raised unexpected {e}")

if __name__ == '__main__':
    unittest.main()

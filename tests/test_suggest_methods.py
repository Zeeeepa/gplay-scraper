"""
Unit tests for Suggest Methods
"""

import unittest
import time
import warnings
from gplay_scraper import GPlayScraper
from gplay_scraper.exceptions import GPlayScraperError, NetworkError, RateLimitError


class TestSuggestMethods(unittest.TestCase):
    """Test suite for suggest methods (search suggestions)."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.scraper = GPlayScraper()
        self.term = "fitness"  # Search term for testing
    
    def test_suggest_analyze(self):
        """Test suggest_analyze returns list of suggestions."""
        time.sleep(2)
        try:
            result = self.scraper.suggest_analyze(self.term, count=5)
            self.assertIsInstance(result, list)
            if result:
                self.assertGreater(len(result), 0)
        except (NetworkError, RateLimitError, GPlayScraperError) as e:
            warnings.warn(f"Network/Rate limit error in test_suggest_analyze: {e}")
            self.skipTest(f"Skipping due to network/rate limit: {e}")
    
    def test_suggest_nested(self):
        """Test suggest_nested returns nested suggestions."""
        time.sleep(2)
        try:
            result = self.scraper.suggest_nested(self.term, count=3)
            self.assertIsInstance(result, dict)
        except (NetworkError, RateLimitError, GPlayScraperError) as e:
            warnings.warn(f"Network/Rate limit error in test_suggest_nested: {e}")
            self.skipTest(f"Skipping due to network/rate limit: {e}")
    
    def test_suggest_print_nested(self):
        """Test suggest_print_nested executes without error."""
        time.sleep(2)
        try:
            self.scraper.suggest_print_nested(self.term, count=3)
        except (NetworkError, RateLimitError, GPlayScraperError) as e:
            warnings.warn(f"Network/Rate limit error in test_suggest_print_nested: {e}")
            self.skipTest(f"Skipping due to network/rate limit: {e}")
        except Exception as e:
            self.fail(f"suggest_print_nested raised unexpected {e}")
    
    def test_suggest_print_all(self):
        """Test suggest_print_all executes without error."""
        time.sleep(2)
        try:
            self.scraper.suggest_print_all(self.term, count=5)
        except (NetworkError, RateLimitError, GPlayScraperError) as e:
            warnings.warn(f"Network/Rate limit error in test_suggest_print_all: {e}")
            self.skipTest(f"Skipping due to network/rate limit: {e}")
        except Exception as e:
            self.fail(f"suggest_print_all raised unexpected {e}")

if __name__ == '__main__':
    unittest.main()

"""
Unit tests for Search Methods
"""

import unittest
import time
import warnings
from gplay_scraper import GPlayScraper
from gplay_scraper.exceptions import GPlayScraperError, NetworkError, RateLimitError


class TestSearchMethods(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.scraper = GPlayScraper()
        cls.query = "social media"
        cls.count = 10
        cls.lang = "en"
        cls.country = "us"
    
    def test_search_analyze(self):
        """Test search_analyze returns list of results"""
        time.sleep(2)
        try:
            result = self.scraper.search_analyze(self.query, count=self.count, lang=self.lang, country=self.country)
            self.assertIsInstance(result, list)
            if result:
                self.assertGreater(len(result), 0)
                self.assertIn('title', result[0])
        except (NetworkError, RateLimitError, GPlayScraperError) as e:
            warnings.warn(f"Network/Rate limit error in test_search_analyze: {e}")
            self.skipTest(f"Skipping due to network/rate limit: {e}")
    
    def test_search_get_field(self):
        """Test search_get_field returns list of field values"""
        time.sleep(2)
        try:
            result = self.scraper.search_get_field(self.query, "title", count=self.count, lang=self.lang, country=self.country)
            self.assertIsInstance(result, list)
            if result:
                self.assertGreater(len(result), 0)
        except (NetworkError, RateLimitError, GPlayScraperError) as e:
            warnings.warn(f"Network/Rate limit error in test_search_get_field: {e}")
            self.skipTest(f"Skipping due to network/rate limit: {e}")
    
    def test_search_get_fields(self):
        """Test search_get_fields returns list of dictionaries"""
        time.sleep(2)
        fields = ["title", "score"]
        try:
            result = self.scraper.search_get_fields(self.query, fields, count=self.count, lang=self.lang, country=self.country)
            self.assertIsInstance(result, list)
            if result:
                self.assertGreater(len(result), 0)
                for field in fields:
                    self.assertIn(field, result[0])
        except (NetworkError, RateLimitError, GPlayScraperError) as e:
            warnings.warn(f"Network/Rate limit error in test_search_get_fields: {e}")
            self.skipTest(f"Skipping due to network/rate limit: {e}")
    
    def test_search_print_field(self):
        """Test search_print_field executes without error"""
        time.sleep(2)
        try:
            self.scraper.search_print_field(self.query, "title", count=5, lang=self.lang, country=self.country)
        except (NetworkError, RateLimitError, GPlayScraperError) as e:
            warnings.warn(f"Network/Rate limit error in test_search_print_field: {e}")
            self.skipTest(f"Skipping due to network/rate limit: {e}")
        except Exception as e:
            self.fail(f"search_print_field raised unexpected {type(e).__name__}: {e}")
    
    def test_search_print_fields(self):
        """Test search_print_fields executes without error"""
        time.sleep(2)
        try:
            self.scraper.search_print_fields(self.query, ["title", "score"], count=5, lang=self.lang, country=self.country)
        except (NetworkError, RateLimitError, GPlayScraperError) as e:
            warnings.warn(f"Network/Rate limit error in test_search_print_fields: {e}")
            self.skipTest(f"Skipping due to network/rate limit: {e}")
        except Exception as e:
            self.fail(f"search_print_fields raised unexpected {type(e).__name__}: {e}")
    
    def test_search_print_all(self):
        """Test search_print_all executes without error"""
        time.sleep(2)
        try:
            self.scraper.search_print_all(self.query, count=5, lang=self.lang, country=self.country)
        except (NetworkError, RateLimitError, GPlayScraperError) as e:
            warnings.warn(f"Network/Rate limit error in test_search_print_all: {e}")
            self.skipTest(f"Skipping due to network/rate limit: {e}")
        except Exception as e:
            self.fail(f"search_print_all raised unexpected {type(e).__name__}: {e}")


if __name__ == '__main__':
    unittest.main()

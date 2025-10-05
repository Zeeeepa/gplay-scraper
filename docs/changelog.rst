Changelog
=========

All notable changes to this project will be documented in this file.

Version 1.0.0 (2024-12-19)
---------------------------

**Added**

- Initial release of GPlay Scraper
- Complete Google Play Store app data extraction
- ASO (App Store Optimization) analysis
- Modular architecture with separate core modules
- Support for 65+ data fields including:

  - Basic app information
  - Install statistics and metrics
  - Ratings and reviews data
  - Technical specifications
  - Developer information
  - Media content (screenshots, videos, icons)
  - Pricing and monetization details
  - ASO keyword analysis

- Multiple access methods:

  - ``analyze()`` - Complete app analysis
  - ``get_field()`` - Single field retrieval
  - ``get_fields()`` - Multiple field retrieval
  - ``print_field()`` - Direct field printing
  - ``print_fields()`` - Multiple field printing
  - ``print_all()`` - Complete data printing as JSON

- Comprehensive documentation and examples
- Error handling and logging
- Rate limiting considerations
- Cross-platform compatibility
- Professional Sphinx documentation
- GitHub Actions CI/CD pipeline
- Comprehensive unit tests

**Features**

- Web scraping of Google Play Store pages
- JSON data extraction and parsing
- Automatic install metrics calculation
- Keyword frequency analysis
- Readability scoring
- Review data extraction
- Image URL processing
- Date parsing and age calculation
- Configuration system with sensible defaults
- Professional logging setup
- Rate limiting for responsible scraping
#!/usr/bin/env python3
"""
Simple test script to verify gplay-scraper package functionality
This script tests basic import and initialization without network calls
"""

def test_import():
    """Test package import"""
    try:
        from gplay_scraper import GPlayScraper
        print("✓ Successfully imported GPlayScraper")
        return True
    except ImportError as e:
        print(f"✗ Failed to import GPlayScraper: {e}")
        return False

def test_initialization():
    """Test scraper initialization"""
    try:
        from gplay_scraper import GPlayScraper
        scraper = GPlayScraper()
        print("✓ Successfully initialized GPlayScraper")
        return True
    except Exception as e:
        print(f"✗ Failed to initialize GPlayScraper: {e}")
        return False

def test_http_clients():
    """Test different HTTP client initializations"""
    from gplay_scraper import GPlayScraper
    
    clients = ["requests", "curl_cffi", "httpx", "urllib3"]
    success_count = 0
    
    for client in clients:
        try:
            scraper = GPlayScraper(http_client=client)
            print(f"✓ Successfully initialized with {client}")
            success_count += 1
        except ImportError:
            print(f"⚠ {client} not available (optional dependency)")
        except Exception as e:
            print(f"✗ Failed to initialize with {client}: {e}")
    
    return success_count > 0

def test_methods_exist():
    """Test that all expected methods exist"""
    from gplay_scraper import GPlayScraper
    scraper = GPlayScraper()
    
    method_groups = [
        ("app", ["analyze", "get_field", "get_fields", "print_field", "print_fields", "print_all"]),
        ("search", ["analyze", "get_field", "get_fields", "print_field", "print_fields", "print_all"]),
        ("reviews", ["analyze", "get_field", "get_fields", "print_field", "print_fields", "print_all"]),
        ("developer", ["analyze", "get_field", "get_fields", "print_field", "print_fields", "print_all"]),
        ("similar", ["analyze", "get_field", "get_fields", "print_field", "print_fields", "print_all"]),
        ("list", ["analyze", "get_field", "get_fields", "print_field", "print_fields", "print_all"]),
        ("suggest", ["analyze", "nested", "print_all", "print_nested"]),
    ]
    
    all_methods_exist = True
    for group, methods in method_groups:
        for method in methods:
            method_name = f"{group}_{method}"
            if hasattr(scraper, method_name):
                print(f"✓ Method {method_name} exists")
            else:
                print(f"✗ Method {method_name} missing")
                all_methods_exist = False
    
    return all_methods_exist

def main():
    """Run all tests"""
    print("Testing gplay-scraper package...")
    print("=" * 50)
    
    tests = [
        ("Import Test", test_import),
        ("Initialization Test", test_initialization),
        ("HTTP Clients Test", test_http_clients),
        ("Methods Existence Test", test_methods_exist),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n{test_name}:")
        try:
            if test_func():
                passed += 1
        except Exception as e:
            print(f"✗ {test_name} failed with exception: {e}")
    
    print("\n" + "=" * 50)
    print(f"Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All basic tests passed! Package is working correctly.")
        return 0
    else:
        print("⚠ Some tests failed. Check the output above.")
        return 1

if __name__ == "__main__":
    exit(main())
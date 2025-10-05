#!/usr/bin/env python3
"""Build documentation using Sphinx."""

import os
import sys
import subprocess
from pathlib import Path

def install_docs_requirements():
    """Install documentation requirements."""
    print("[INFO] Installing documentation requirements...")
    try:
        subprocess.run([
            sys.executable, "-m", "pip", "install", 
            "-r", "docs/requirements.txt"
        ], check=True)
        print("[OK] Documentation requirements installed!")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Failed to install requirements: {e}")
        return False
    return True

def build_html_docs():
    """Build HTML documentation."""
    print("[INFO] Building HTML documentation...")
    
    docs_dir = Path("docs")
    build_dir = docs_dir / "_build" / "html"
    
    try:
        # Change to docs directory
        os.chdir(docs_dir)
        
        # Build documentation
        subprocess.run([
            "sphinx-build", "-b", "html", ".", "_build/html"
        ], check=True)
        
        print("[OK] Documentation built successfully!")
        print(f"[INFO] Open: {Path('_build/html/index.html').absolute()}")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Failed to build documentation: {e}")
        return False
    except FileNotFoundError:
        print("[ERROR] Sphinx not found. Installing requirements first...")
        return False

def main():
    """Main function to build documentation."""
    print("=== GPlay Scraper Documentation Builder ===\n")
    
    # Install requirements
    if not install_docs_requirements():
        return 1
    
    # Build documentation
    if not build_html_docs():
        return 1
    
    print("\n[SUCCESS] Documentation build complete!")
    print("[INFO] Open docs/_build/html/index.html in your browser")
    return 0

if __name__ == "__main__":
    sys.exit(main())
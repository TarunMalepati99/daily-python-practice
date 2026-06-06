#!/usr/bin/env python3
"""
Daily Python Practice Script
This script runs daily as part of the GitHub Actions workflow.
"""

import datetime

def main():
    """Main function for daily practice."""
    print("Daily Python Practice")
    print(f"Timestamp: {datetime.datetime.now()}")
    
    # Write to example.txt
    with open("example.txt", "w") as f:
        f.write(f"Last updated: {datetime.datetime.now()}\n")
    
    print("Completed daily practice!")

if __name__ == "__main__":
    main()
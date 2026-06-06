#!/usr/bin/env python3
"""Daily Python practice script."""

from datetime import datetime

# Get current date
current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Write to example.txt
with open('example.txt', 'a') as f:
    f.write(f"Daily practice executed at: {current_date}\n")

print(f"Daily practice script executed at {current_date}")

#!/usr/bin/python3
"""
This script sends a request to the URL, then displays
the body of the response and handles errors if occured.
"""

import requests
import sys

if __name__ == "__main__":

    response = requests.get(sys.argv[1])

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)

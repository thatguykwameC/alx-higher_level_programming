#!/usr/bin/python3
"""
This script displays the value of the X-Request-Id variable
found in the header of the response with Requests library
"""

import requests
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))

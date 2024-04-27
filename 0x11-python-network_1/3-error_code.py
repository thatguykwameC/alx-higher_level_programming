#!/usr/bin/python3
"""
This script sends a request to the URL and displays
the body of the response and handles errors if occured.
"""

from urllib.request import Request, urlopen
from urllib.error import HTTPError
import sys

if __name__ == "__main__":

    req = Request(sys.argv[1])

    try:
        with urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as error:
        print('Error code: {}'.format(error.code))

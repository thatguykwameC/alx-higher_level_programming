#!/usr/bin/python3
"""This script sends a POST request to the url with the email as a parameter"""

import requests
import sys

if __name__ == "__main__":

    email = {'email': sys.argv[2]}
    response = requests.post(sys.argv[1], email)
    print(response.text)

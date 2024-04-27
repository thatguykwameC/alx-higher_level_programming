#!/usr/bin/python3
"""
This script sends a POST request with the email
as a parameter and displays the body of the response
"""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":

    email = {'email': sys.argv[2]}
    enc_data = urllib.parse.urlencode(email).encode('utf-8')
    request = urllib.request.Request(sys.argv[1], enc_data)

    with urllib.request.urlopen(request) as response:
        response_body = response.read()
        print(response_body.decode('utf-8'))

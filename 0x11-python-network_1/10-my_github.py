#!/usr/bin/python3
"""
This script takes my GitHub credentials and
uses it's API to display my id
"""

import requests
import sys

if __name__ == "__main__":

    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(url, auth=(username, password))
    print(response.json().get('id'))

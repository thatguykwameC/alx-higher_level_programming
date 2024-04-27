#!/usr/bin/python3
"""
This script takes my GitHub credentials and
uses it's API to display my id
"""

import requests
import sys

if __name__ == "__main__":

    url = "https://api.github.com/user"
    user = sys.argv[1]
    passwd = sys.argv[2]
    req = requests.get(url, auth=(user, passwd))
    print(req.json().get('id'))

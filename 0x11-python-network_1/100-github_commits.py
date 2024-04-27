#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of the repository and user
sent in as arguments
"""

import requests
from sys import argv

if __name__ == '__main__':

    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    response = requests.get(url)

    commits = response.json()[:10]
    for commit in commits:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))

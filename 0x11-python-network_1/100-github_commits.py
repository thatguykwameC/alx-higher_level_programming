#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of the repository and user
sent in as arguments
"""

import requests
import sys
from sys import argv, exit

if __name__ == '__main__':

    if len(argv) < 3:
        print(f"Usage: {argv[0]} <repo> <owner>")
        exit(1)

    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error: Not a valid repository")
        exit(1)

    commits = response.json()[:10]
    for commit in commits:
        sha = commit['sha']
        author = commit['commit']['author']['name']
        print(f"{sha}: {author}")

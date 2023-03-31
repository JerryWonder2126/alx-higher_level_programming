#!/usr/bin/python3
"""
Gets the last 10 commits in a repo
Usage:
    ./100-github_commits.py <owner> <repo>
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    owner, repo = sys.argv[1:]
    r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/commits",
                     headers=headers)
    try:
        for i in range(10):
            print("{}: {}".format(
                r.json()[i]['sha'],
                r.json()[i]['commit']['author']['name']
            ))
    except IndexError:
        pass

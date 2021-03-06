#!/usr/bin/python3
"""
Python script that takes your Github credentials (username and password)
and uses the Github API to display your id
"""

if __name__ == "__main__":
    import requests
    import sys

    r = requests.get(
        'https://api.github.com/user',
        auth=(
            sys.argv[1],
            sys.argv[2]))
    a_dict = r.json()
    print(a_dict.get("id"))

#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""

if __name__ == "__main__":
    import urllib.request
    import sys
    from urllib import parse

    data = {'email': sys.argv[2]}
    encoded_data = parse.urlencode(data).encode('utf-8')
    url = sys.argv[1]

    with urllib.request.urlopen(url, encoded_data) as response:
        print(response.read().decode('utf-8'))

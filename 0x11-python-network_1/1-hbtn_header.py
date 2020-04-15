#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL and displays
    the value of the X-Request-Id variable found in the header of the response
"""


import urllib.request
import sys


def init():
    """ Executes the program """
    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.getheader('X-Request-Id'))
        print(response.getheaders())


if __name__ == "__main__":
    """ Assures that the module won't be executed if imported """
    init()

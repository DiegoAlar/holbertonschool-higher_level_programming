#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status """


import urllib.request


def init():
    """ Executes the program """
    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
    print('Body response:')
    print('\t- type: {}'.format(type(html)))
    print('\t- content: {}'.format(html))
    print('\t- utf8 content: {}'.format(html.decode("utf-8")))


if __name__ == "__main__":
    """ Assures that the module won't be executed if imported """
    init()

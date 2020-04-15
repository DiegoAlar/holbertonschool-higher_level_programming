#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
if __name__ == "__main__":
    import requests
    import sys
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        letter = {'q': sys.argv[1]}
    else:
        letter = {'q': ""}
    r = requests.post(url, data=letter)
    r.encoding = 'utf-8'
    a_dict = r.json()
    if type(a_dict == dict):
        if len(a_dict) == 0:
            print('No result')
        else:
            print("[{}] {}".format(a_dict['id'], a_dict['name']))
    else:
        print('Not a valid JSON')

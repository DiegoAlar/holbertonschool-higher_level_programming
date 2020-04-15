#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
if __name__ == "__main__":
    import requests
    import sys
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 2:
        letter = {'q': sys.argv[1]}
        r = requests.post(url, data=letter)
        if r.json is not None:
            try:
                a_dict = r.json()
                print("[{}] {}".format(a_dict['id'], a_dict['name']))
            except ValueError:
                print("Not a valid JSON")
    else:
        print('No result')

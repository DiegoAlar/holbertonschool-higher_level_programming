#!/usr/bin/python3
""" This module contains function save_to_json_file
"""


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file, using a
    JSON representation:
    Args:
        my_obj (obj): the object to be copied
        filename (file): to file
    """
    import json
    
    with open(filename, "w", encoding="utf-8") as my_file:
        json.dump(my_obj, my_file)

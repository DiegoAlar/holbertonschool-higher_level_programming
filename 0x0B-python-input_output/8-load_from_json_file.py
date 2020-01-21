#!/usr/bin/python3
""" This module contains function load_from_json_file
"""


def load_from_json_file(filename):
    """
    Function that creates an Object from a “JSON file”
    Args:
        filename (file): the file to be opened
    """
    import json
    with open(filename, encoding="utf-8") as my_file:
        j_file = json.load(my_file)
        return j_file

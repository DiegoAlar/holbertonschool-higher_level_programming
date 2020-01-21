#!/usr/bin/python3
""" This module contains function from_json_string
"""


def from_json_string(my_str):
    """
            function that returns an object (Python data structure)
            represented by a JSON string:
            Args:
                my_str (str): string to be converted to json obj
    """
    import json
    return json.loads(my_str)

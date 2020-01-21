#!/usr/bin/python3
""" this module contains function to_json_string
"""


def to_json_string(my_obj):
    """ this function  returns the JSON representation of an object (string)
        Args:
            my_obj (obj): object
    """
    import json
    return json.dumps(my_obj)

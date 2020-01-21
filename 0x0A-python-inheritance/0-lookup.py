#!/usr/bin/python3
""" This module contains lookup function
"""


def lookup(obj):
    """ Returns the list of available attributes and methods of an object
    Args:
        obj (obj): and object
    """
    return dir(obj)

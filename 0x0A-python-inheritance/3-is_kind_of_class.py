#!/usr/bin/python3
""" This module contains function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
        finds out if instance is of type of a given class
        Args:
            obj (obj): the object
            a_class (class): a class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False

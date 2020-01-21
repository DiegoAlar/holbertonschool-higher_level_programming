#!/usr/bin/python3
""" This module contains function is_same_class
"""


def is_same_class(obj, a_class):
    """
        Function that returns True or False if instance off
        Args:
            obj (obj): the object
            a_class: the class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False

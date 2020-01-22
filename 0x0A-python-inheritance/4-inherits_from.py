#!/usr/bin/python3
""" This module contains function inherits_from
"""


def inherits_from(obj, a_class):
    """"
        This function will find if the object is an instance of a class
        that inherited (directly or indirectly) from the specified class
        Args:
            obj (obj): the object
            a_class (class): the class
    """
    if issubclass(type(obj), a_class) and not type(obj) is not a_class:
        return False
    else:
        return True

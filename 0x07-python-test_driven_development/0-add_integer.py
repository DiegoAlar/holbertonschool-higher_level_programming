#!/usr/bin/python3
""" this module contains function add_integer
        Args:
            a (int): first number to add
            b (int): number to be added with a
"""


def add_integer(a, b=98):
    """
            Function that adds two integers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)

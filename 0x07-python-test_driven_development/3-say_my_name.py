#!/usr/bin/python3
""" This module contains function say_my_name
        Args:
            first_name (string): user's first name
            last_name (string): user's last name
"""


def say_my_name(first_name, last_name=""):
    """
            Function that prints a user's name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))

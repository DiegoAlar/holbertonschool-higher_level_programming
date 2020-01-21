#!/usr/bin/python3
""" This module contains function readfile
"""


def read_file(filename=""):
    """ This function reads a file
    Args:
        filename (file): the file to read
    """
    with open(filename, encoding="utf-8") as my_file:
        for line in my_file:
            print(line, end="")

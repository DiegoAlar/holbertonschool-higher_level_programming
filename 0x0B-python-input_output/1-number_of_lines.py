#!/usr/bin/python3
""" This module contains function number_of_lines
"""


def number_of_lines(filename=""):
    """
    This function returns number of lines of a file
    Args:
        filename (file): the file to be opened
    """
    with open(filename, encoding="utf-8") as my_file:
        lines = 0
        for line in my_file:
            lines += 1
        return lines

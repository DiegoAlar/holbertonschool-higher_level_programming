#!/usr/bin/python3
""" This module contains function write_file
"""


def write_file(filename="", text=""):
    """
    This function writes on a file
    Args:
        filename (file): a file
        text (str): string to write to file
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        return my_file.write(text)

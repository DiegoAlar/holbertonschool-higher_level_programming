#!/usr/bin/python3
""" This module contains function append_write
"""


def append_write(filename="", text=""):
    """ function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added:
    Args:
        filename (file): the file
        text (text): the text to append string at the end
    """
    with open(filename, "a", encoding="utf-8") as my_file:
        txt = text
        if not isinstance(type(text), str):
            txt = str(text)
        return my_file.write(txt)

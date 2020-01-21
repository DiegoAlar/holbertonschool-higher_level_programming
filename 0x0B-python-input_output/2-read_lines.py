#!/usr/bin/python3
""" This module contains function read_lines
"""


def read_lines(filename="", nb_lines=0):
    """ this module read lines of a file given the number of lines
        Args: 
            filename (file): to file to be opened
            nb_lines (int): number of lines to be printed
    """
    with open(filename, encoding="utf-8") as my_file:
        lines = 0
        for line in my_file:
            lines += 1
            if lines == nb_lines:
                print(line, end="")
                break
            else:
                print(line, end="")

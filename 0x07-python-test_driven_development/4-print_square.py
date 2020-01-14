#!/usr/bin/python3
""" this module only contains print_square function """
def print_square(size):
    """
    function that prints a square with the character #
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0 and type(size) is int:
        raise ValueError("size must be >= 0")
    elif size < 0 and type(size) is float:
        raise TypeError("size must be an integer")
    for i in range(size):
        for k in range(size):
            print("#", end="")
        print()

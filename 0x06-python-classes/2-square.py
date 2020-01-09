#!/usr/bin/python3
class Square:
    """Class that defines instance given size"""
    def __init__(self, size=0):
        """init method to initialized variables
        Args:
            size (int): the size of the square.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

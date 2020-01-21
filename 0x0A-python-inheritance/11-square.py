#!/usr/bin/python3
""" class that uses str magic method
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class that inherits from Rectangle
    """

    def __init__(self, size):
        """
                Constructor
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
                defines area of sqaure
        """
        return self.__size ** 2

    def __str__(self):
        """ magic method
        """
        return "[Square] " + str(self.__size) + "/" + str(self.__size)

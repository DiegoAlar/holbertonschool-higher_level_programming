#!/usr/bin/python3
""" This module contains empty class BaseGeometry
"""


class BaseGeometry:
    """
            class BaseGeometry empty
    """

    def area(self):
        """ Function that raises an error
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ method that validates value
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value < 1:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
        class that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
                constructor
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ defines area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """ string representation of rectangle class
        """
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)


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

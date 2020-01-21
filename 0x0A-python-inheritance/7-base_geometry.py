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

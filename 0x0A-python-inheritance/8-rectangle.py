#!/usr/bin/python3
""" This module contains empty class BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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

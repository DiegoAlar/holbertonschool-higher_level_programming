#!/usr/bin/python3
"""
This module contains class Rectangle that inherits from Base
"""


from models.base import Base


class Rectangle(Base):
    """
    This class defines a Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor of Rectangle class
        """
        __dict_args = {"width": width, "height": height, "x": x, "y": y}
        self.__input_validator(__dict_args)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        a_dict = {"width": width}
        self.__input_validator(a_dict)
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        a_dict = {"height": height}
        self.__input_validator(a_dict)
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        a_dict = {"x": x}
        self.__input_validator(a_dict)
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        a_dict = {"y": y}
        self.__input_validator(a_dict)
        self.__y = y

    def __input_validator(self, a_dict):
        """ private method to validate user's inpu
        """
        for k, v in a_dict.items():
            if type(v) is not int:
                raise TypeError("{} must be an integer".format(k))
            elif k is "width" and v < 1:
                raise ValueError("{} must be > 0".format(k))
            elif k is "height" and v < 1:
                raise ValueError("{} must be > 0".format(k))
            elif k is "x" and v < 0:
                raise ValueError("{} must be >= 0".format(k))
            elif k is "y" and v < 0:
                raise ValueError("{} must be >= 0".format(k))

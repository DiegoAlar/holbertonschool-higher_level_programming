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
        self.input_validator(__dict_args)
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
        self.input_validator(a_dict)
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        a_dict = {"height": height}
        self.input_validator(a_dict)
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        a_dict = {"x": x}
        self.input_validator(a_dict)
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        a_dict = {"y": y}
        self.input_validator(a_dict)
        self.__y = y

    def area(self):
        """ returns the area value of the Rectangle instance
        """
        return self.width * self.height

    def display(self):
        """ prints in stdout the Rectangle instance with the character #
        """
        mg_w = self.width
        mg_h = self.height
        str_to_prt = "\n" * self.y + (" " * self.x + "#" * mg_w + '\n') * mg_h
        print(str_to_prt[:-1])

    def __str__(self):
        """ overrides str function to print str representation of class
            rectangle
        """
        mge = "[Rectangle] ({}) {}/{} - {}/{}"
        return mge.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute
        """
        list_args = ["id", "width", "height", "x", "y"]
        count = 0
        a_dict = {}

        if args:
            if len(args) > 0 and len(args) < 6:
                for arg in args:
                    a_dict.update({list_args[count]: arg})
                    count += 1
                    setattr(self, list_args[count], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def update_args(self, a_dict):
        """ Private method to update args given *args or **kwargs
        """
        for k, v in a_dict.items():
            if k is "id":
                self.id = v
            elif k is "width":
                self.__width = v
            elif k is "height":
                self.__height = v
            elif k is "x":
                self.__x = v
            elif k is "y":
                self.__y = v

    def to_dictionary(self):
        """ Returns the dictionary representation of a Rectangle:
        """
        a_dictionary = {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width}
        return a_dictionary

    def input_validator(self, a_dict):
        """ private method to validate user's input
        """
        print("entered")
        for k, v in a_dict.items():
            if not isinstance(v, int):
                raise TypeError("{} must be an integer".format(k))
            elif k == "width" and v < 1:
                raise ValueError("{} must be > 0".format(k))
            elif k is "height" and v < 1:
                raise ValueError("{} must be > 0".format(k))
            elif k is "x" and v < 0:
                raise ValueError("{} must be >= 0".format(k))
            elif k is "y" and v < 0:
                raise ValueError("{} must be >= 0".format(k))

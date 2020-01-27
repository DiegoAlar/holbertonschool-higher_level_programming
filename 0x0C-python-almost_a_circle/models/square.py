#!/usr/bin/python3
""" This module contains class Square that inherits from Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ This class defines a Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ This is the class constructor
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 1:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute
        """
        list_args = ["id", "size", "x", "y"]
        count = 0
        a_dict = {}

        if args:
            if len(args) > 0 and len(args) < 5:
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
            elif k is "size":
                self.size = v
            elif k is "x":
                self.x = v
            elif k is "y":
                self.y = v

    def to_dictionary(self):
        """ Returns the dictionary representation of a Square
        """
        a_dict = {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y}
        return a_dict

    def input_validator(self, a_dict):
        """ private method to validate user's input
        """
        for k, v in a_dict.items():
            if not isinstance(v, int):
                raise TypeError("{} must be an integer".format(k))
            elif k is "size" and v < 1:
                raise ValueError("{} must be > 0".format(k))
            elif k is "x" and v < 0:
                raise ValueError("{} must be >= 0".format(k))
            elif k is "y" and v < 0:
                raise ValueError("{} must be >= 0".format(k))

    def __str__(self):
        """ String representation of the Square class
        """
        mge = "[Square] ({}) {}/{} - {}"
        return mge.format(self.id, self.x, self.y, self.width)

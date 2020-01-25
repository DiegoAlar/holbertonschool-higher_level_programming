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

    def __str__(self):
        """ String representation of the Square class
        """
        mge = "[Square] ({}) {}/{} - {}"
        return mge.format(self.id, self.x, self.y, self.width)

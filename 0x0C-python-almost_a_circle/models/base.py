#!/usr/bin/python3
""" This module contains class Base
"""


class Base:
    """
    This is the base class for square and rectangle subclasses
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor of the base class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

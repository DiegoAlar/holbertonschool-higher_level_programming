#!/usr/bin/python3
""" this module contains class Student
"""


class Student:
    """ class that defines an student
    """
    def __init__(self, first_name, last_name, age):
        """
        constructor
        Args:
            first_name (str): first name
            last_name (str): last name
            age (int): the age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrieves a dictionary representation of a Student instance
        """
        return self.__dict__

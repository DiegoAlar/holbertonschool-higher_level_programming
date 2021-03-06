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

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student instance
        """
        vals = self.__dict__
        if attrs is None:
            return vals
        my_dic = {}
        for item in attrs:
            if item in vals:
                my_dic[item] = vals[item]
        return my_dic

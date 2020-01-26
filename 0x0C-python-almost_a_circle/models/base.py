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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries
        """
        import json
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file
        """
        import json
        obj_list = []

        if list_objs is not None:
            for obj in list_objs:
                obj_list.append(obj.to_dictionary())
        json_dictionary = cls.to_json_string(obj_list)
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as my_file:
            return my_file.write(json_dictionary)

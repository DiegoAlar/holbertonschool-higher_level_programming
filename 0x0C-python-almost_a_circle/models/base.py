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
            my_file.write(json_dictionary)

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string
        """
        import json
        a_list = []
        if json_string is None or json_string is "":
            return a_list
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy_obj = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_obj = cls(1)
        dummy_obj.update(**dictionary)
        return dummy_obj

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances
        """
        import json
        import os

        if cls.__name__ == "Rectangle":
            file_path = "Rectangle.json"
        elif cls.__name__ == "Square":
            file_path = "Square.json"

        if os.path.exists(file_path):
            list_inst = []
            with open(file_path, "r", encoding="utf-8") as my_file:
                json_data = cls.from_json_string(my_file.read())
            for obj in json_data:
                list_inst.append(cls.create(**obj))
            return list_inst
        else:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ text
        """
        import json
        obj_list = []

        if list_objs is not None:
            for obj in list_objs:
                obj_list.append(obj.to_dictionary())
        json_dictionary = cls.to_json_string(obj_list)
        with open(cls.__name__ + ".csv", "w", encoding="utf-8") as my_file:
            my_file.write(json_dictionary)

    @classmethod
    def load_from_file_csv(cls):
        """ Text
        """
        import json
        import os

        if cls.__name__ == "Rectangle":
            file_path = "Rectangle.csv"
        elif cls.__name__ == "Square":
            file_path = "Square.csv"

        if os.path.exists(file_path):
            list_inst = []
            with open(file_path, "r", encoding="utf-8") as my_file:
                json_data = cls.from_json_string(my_file.read())
            for obj in json_data:
                list_inst.append(cls.create(**obj))
            return list_inst
        else:
            return []

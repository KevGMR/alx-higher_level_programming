#!/usr/bin/python3
"""
Contains class Base
assigns id to class even if id
is not assigned
"""
import json


class Base:
    """Initializes new base"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns list dictionaries"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves to json file"""
        file_name = cls.__name__ + ".json"
        text = []

        if list_objs:
            for lst in list_objs:
                text.append(lst.to_dictionary())
        with open(file_name, mode="w", encoding="utf-8") as f:
            return f.write(Base.to_json_string(text))

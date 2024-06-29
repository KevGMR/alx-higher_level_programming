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

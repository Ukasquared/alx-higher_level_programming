#!/usr/bin/python3

"""base.py module"""
import json

class Base:
    """ definining attributes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """base of all other class"""
        if id is None:
            Base.__nb_objects += 1
        self.id = id if id is not None else Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if type(list_dictionaries) is None:
            return "[]"
        json_string = json.dumps(list_dictionaries)
        return json_string

    @classmethod
    def save_to_file(cls, list_objs):
        file_name = cls.__name__ + ".json"
        with open(file_name, 'w') as json_file:
            if type(list_objs) is None:
                json_file.write("[]")
            list_dicts = [dicts.to_dictionary() for dicts in list_objs]
            json_file.write(cls.to_json_string(list_dicts))


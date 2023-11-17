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
        """ this method converts list of
        of dictionaries to json string """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        json_string = json.dumps(list_dictionaries)
        return json_string

    @classmethod
    def save_to_file(cls, list_objs):
        """ converts list of instance to list of
        dictionaries and then to json string,
        and writes the data to a file """
        file_name = cls.__name__ + ".json"
        with open(file_name, 'w') as json_file:
            if type(list_objs) is None or len(list_objs) == 0:
                json_file.write("[]")
            else:
                list_dicts = [dicts.to_dictionary() for dicts in list_objs]
                json_file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ this method converts list of
        of dictionaries to json string """
        if json_string is None:
            return []
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ creates a new instance that has
        access to all the attributes and method
        of the class """
        if dictionary and len(dictionary) != 0:
            if cls.__name__ == "Rectangle":
                new_instance = cls(1, 2)
            else:
                new_instance = cls(1)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """ reads from a file
        converts json string to list of
        dictionaries and then to list of instance,
        and writes the data to a file
        """
        file_name = f"{cls.__name__}.json"
        instance_list = []
        try:
            with open(file_name, 'r') as json_file:
                json_data = json_file.read()
                dict_list = cls.from_json_string(json_data)
                for dicts in dict_list:
                    instance_list.append(cls.create(**dicts))
            return instance_list
        except IOError:
            ("cannot open file")
            return []

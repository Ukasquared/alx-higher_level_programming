#!/usr/bin/python3
""" student moduler"""


class Student:
    """ student class
    """
    def __init__(self, firstname, lastname, age):
        """ instantiates the instance
        with these attributes """
        self.first_name = firstname
        self.last_name = lastname
        self.age = age

    def to_json(self, attrs=None):
        """ convert to dictionary
        """
        to_dict = self.__dict__
        to_dict1 = {}
        if attrs is not None:
            for key, value in to_dict.items():
                for attr in attrs:
                    if attr == key:
                        to_dict1[attr] = value
            return to_dict1
        return to_dict

    def reload_from_json(self, json):
        """ deserialization """
        for key, values in json.items():
            setattr(self, key, values)

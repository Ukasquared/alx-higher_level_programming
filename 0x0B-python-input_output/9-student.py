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

    def to_json(self):
        """ to json """
        to_dict = self.__dict__
        return to_dict

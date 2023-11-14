#!/usr/bin/python3

"""base.py module"""


class Base:
    """ definining attributes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """base of all other class"""
        if id is None:
            Base.__nb_objects += 1
        self.id = id if id is not None else Base.__nb_objects

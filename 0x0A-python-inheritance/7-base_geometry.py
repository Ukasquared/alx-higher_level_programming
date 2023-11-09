#!/usr/bin/python3

""" the BaseGeometry module"""


class BaseGeometry:
    """ perform basic calculation"""
    def area(self):
        """ compute area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validatec the integer """
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

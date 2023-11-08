#!/usr/bin/python3

""" same class module"""


def is_same_class(obj, a_class):
    """ function that returns True if
    the object is exactly an instance
    of the specified class """
    return obj.__class__ is a_class

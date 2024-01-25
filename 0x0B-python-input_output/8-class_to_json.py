#!/usr/bin/python3
""" class_to_json module"""


def class_to_json(obj):
    """ converts class to
    dictionary and to json
    """
    to_dict = obj.__dict__
    return to_dict

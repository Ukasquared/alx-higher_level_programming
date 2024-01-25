#!/usr/python3
""" load_from_json_file """
import json


def load_from_json_file(filename):
    """ creates an Object
    from a “JSON file
    """
    with open(filename) as file:
        json_obj = file.read()
        py_obj = json.loads(json_obj)
        return py_obj

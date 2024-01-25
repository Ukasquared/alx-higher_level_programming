#!/usr/bin/python3
""" 4-from_json_string.py mmodule """
import json


def from_json_string(my_str):
    """ converts json objects to python object """
    py_obj = json.loads(my_str)
    return py_obj

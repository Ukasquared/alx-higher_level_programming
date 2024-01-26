#!/usr/bin/python3
""" from_py_to_json module"""
import json
from sys import argv
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def from_py_to_json():
    """ from python object to
    to json object
    """
    old_list = ""
    filename = "add_item.json"
    if os.path.exists(filename):
        old_list = load_from_json_file(filename)
    new_list = [argv[i] for i in range(1, len(argv))]
    if old_list:
        old_list.extend(new_list)
        save_to_json_file(old_list, filename)
    else:
        save_to_json_file(new_list, filename)


from_py_to_json()

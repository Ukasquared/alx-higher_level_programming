#!/usr/bin/python3
""" save_to_json_file """
import json


def save_to_json_file(my_obj, filename):
    """convert to json
    save to a file
    """
    with open(filename, 'w') as file:
        json_obj = json.dumps(my_obj)
        file.write(json_obj)

#!/usr/bin/python3
""" to_json_string module"""
import json

def to_json_string(my_obj):
    serialized_data = json.dumps(my_obj)
    return serialized_data

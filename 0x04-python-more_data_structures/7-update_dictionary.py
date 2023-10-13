#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    dict = {}
    dict[key] = value
    a_dictionary.update(dict)
    return a_dictionary

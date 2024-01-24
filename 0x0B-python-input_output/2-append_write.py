#!/usr/bin/python3
""" append_writ module """

def append_write(filename="", text=""):
    """ appends text to a file """
    with open(filename, "a", encoding="utf-8") as f:
        num_chars = f.write(text)
        return num_chars

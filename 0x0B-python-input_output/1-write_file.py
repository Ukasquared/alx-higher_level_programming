#!/usr/bin/python3
""" write_file module"""

def write_file(filename="", text=""):
    with open(filename, 'w', encoding="utf-8") as f:
        char_num = f.write(text)
        return (char_num)

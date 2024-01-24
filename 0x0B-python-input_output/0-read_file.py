#!/usr/bin/python3
""" read_file module """

def read_file(filename=""):
    """ reads a file"""
    with open(filename, encoding="utf-8") as f:
        read_file = f.read()
    print(read_file)

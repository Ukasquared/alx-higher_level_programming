#!/usr/bin/python3

""" prints a text to the console"""


def text_indentation(text):
    """ identing text"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if (not text[i] == '.' and not text[i] == ':' 
		 and not text[i] == '?'):
            print(text[i], end="")
        else:
            print(text[i])
            print()
            if text[i + 1] == " ":
                i += 1
        i += 1


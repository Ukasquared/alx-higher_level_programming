#!/usr/bin/python3

""" prints a text to the console"""


def text_indentation(text):
    """ identing text"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    new_text = ""
    while i < len(text):
        if (not text[i] == '.' and not text[i] == ':' and not text[i] == '?'):
            new_text += text[i]
        else:
            new_text += text[i]
            new_text += "\n\n"
            i += 1
        i += 1
    print("{}".format(new_text))


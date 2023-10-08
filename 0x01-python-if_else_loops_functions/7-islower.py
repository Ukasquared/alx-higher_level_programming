#!/usr/bin/python3

def islower(c):
    lowerstart = 97
    lowerend = 122
    if ord(c) >= lowerstart and ord(c) <= lowerend:
        return True
    else:
        return False

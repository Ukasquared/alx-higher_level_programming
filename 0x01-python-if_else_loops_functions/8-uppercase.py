#!/usr/bin/python3

def uppercase(str):
    for i in str:
        if ord(i) in range(97, 123):
            cap = chr(ord(i) - 32)
        else:
            cap = i
        print("{}".format(cap), end="")
    print()

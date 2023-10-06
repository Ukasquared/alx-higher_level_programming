#!/usr/bin/python3
import sys


def cmdl():
    """Print the number of and list of arguments."""
    lenn = len(sys.argv) - 1

    if lenn == 0:
        print("0 arguments.")
    elif lenn == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(lenn))
    
    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))
    if __name__ == "__main__":
        cmdl()

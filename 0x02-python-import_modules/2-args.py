#!/usr/bin/python3
import sys


def cmd_line():
    """Print the number of and list of arguments."""
    len_t = len(sys.argv) - 1
    if len_t == 0:
        print("{} arguments.".format(len_t))
    elif len_t == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(len_t))
    for i, arg_m in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg_m))


if __name__ == "__main__":
    cmd_line()

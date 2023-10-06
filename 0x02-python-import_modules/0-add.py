#!/usr/bin/python3
from add_0 import add


def f():
    a = 1
    b = 2
    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))


if __name__ == "__main__":
    f()

#!/usr/bin/python3

"""addition of two integers"""


def add_integer(a, b=98):
    """adds two integers"""
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b

    if __name__ == "__main__":
        import doctest
        doctest.testfile(tests/0-add_integer.txt)

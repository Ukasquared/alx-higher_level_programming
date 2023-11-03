#!/usr/bin/python3

"""addition of two integers"""


def add_integer(a, b=98):
    """adds two integers"""
    if a == None:
        raise TypeError("a must be an integer")
    if b == None:
        raise TypeError("b must be an integer")
    if not a:
        raise TypeError("a must be an integer")
    if not b:
        raise TypeError("b must be an integer")
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, bool):
        raise TypeError("a must be an integer")
    if isinstance(b, bool):
        raise TypeError("b must be an integer")
    if a == float('inf'):
        raise TypeError("a must be an integer")
    if b == float('inf'):
        raise TypeError("b must be an integer")
    if a + 1 == a:
        raise TypeError("a must be an integer")
    if b + 1 == b:
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b

    if __name__ == "__main__":
        import doctest
        doctest.testfile(tests/0-add_integer.txt)

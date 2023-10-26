#!/usr/bin/python3
# define a square module


""" define a module that instatiates its attribute"""


class Square:
    """ handles a square values"""

    def __init__(self, size=0):
        """initializes an instance of the class
        Args:
            self: represents the class
            size: size of square
        """
        if type(size) is int:
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")

    """defines the square area"""
    def area(self):
        """returns the arear"""
        square = self.__size ** 2
        return square

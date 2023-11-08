#!/usr/bin/python3

""" imports the rectangle module """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ instantiation of class """

    def __init__(self, size):
        """ instantiation of instance """
        self.__size = size
        super().integer_validator("size", size)
        super().__init__(size, size)
        super().area()

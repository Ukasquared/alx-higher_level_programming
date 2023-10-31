#!/usr/bin/python3
""" defines a rectangle """


class Rectangle:
    """ instantiates an instance attributes """
    def __init__(self, width=0, height=0):
        """ initialization of attributes
        Args:
            width: represent the width of rectangle
            height: represent the height of this rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if value is less than o
         """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ retrieves the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ returns the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

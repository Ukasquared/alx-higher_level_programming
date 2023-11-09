#!/usr/bin/python3

""" a subclass of BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """computes the size of a rectangle"""
    def __init__(self, width, height):
        """ instance instantiation """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ finding area """
        return self.__width * self.__height

    def __str__(self):
        """ display information to user """
        return f"[{type(self).__name__}] {self.__width}/{self.__height}"

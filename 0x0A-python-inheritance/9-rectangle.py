#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

""" a subclass of BaseGeometry """


class Rectangle(BaseGeometry):
    """computes the size of a rectangle"""

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[{type(self).__name__}] {self.__width}/{self.__height}"

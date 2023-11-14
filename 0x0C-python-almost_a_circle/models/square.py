#!/usr/bin/python3

""" the square model"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """this square class inherits the behaviour of rectanfle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        super().__str__()

    @property
    def size(self):
        return super().width

    @size.setter
    def size(self, new_value):
        super(Square, self).width.__set__(self, new_value)

    @property
    def size_two(self):
        return super().height

    @size_two.setter
    def size_two(self, new_value):
        super(Square, self).height.__set__(self, new_value)

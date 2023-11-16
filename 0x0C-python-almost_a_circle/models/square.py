#!/usr/bin/python3

""" the square model"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """this square class inherits the behaviour of rectanfle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return (f"[{type(self).__name__}] ({self.id}) "
                f"{self.x}/{self.y} {self.width}")

    @property
    def size(self):
        return super().width

    @size.setter
    def size(self, new_value):
        super(Square, Square).width.__set__(self, new_value)

    @property
    def size_two(self):
        return super().height

    @size_two.setter
    def size_two(self, new_value):
        super(Square, Square).height.__set__(self, new_value)

    def update(self, *args, **kwargs):
         super().update(*args, **kwargs)

    def to_dictionary(self):
        return {
            'id': self.id,
            'x': self.x,
            'size': self.width,
	    'y': self.y
            }

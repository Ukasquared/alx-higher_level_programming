#!/usr/bin/python3

""" the square model"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """this square class inherits the behaviour of rectanfle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ return a readable information about
        the object """
        return (f"[{type(self).__name__}] ({self.id}) "
                f"{self.x}/{self.y} {self.width}")

    @property
    def size(self):
        """this returns the size of the
        square """
        return super().width

    @size.setter
    def size(self, new_value):
        """ sets the of the size of the parent class
        which reflect for the square """
        super(Square, Square).width.__set__(self, new_value)

    @property
    def size_two(self):
        """ gets the size of the square"""
        return super().height

    @size_two.setter
    def size_two(self, new_value):
        """ sets the of the size of the parent class
        which reflect for the square
        """
        super(Square, Square).height.__set__(self, new_value)

    def update(self, *args, **kwargs):
        """ update the attributes of the
        instance
        """
        super().update(*args, **kwargs)

    def to_dictionary(self):
        """ converts list to dictionary
        """
        return {
            'id': self.id,
            'x': self.x,
            'size': self.width,
            'y': self.y
            }

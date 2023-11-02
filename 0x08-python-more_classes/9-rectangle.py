#!/usr/bin/python3
""" defines a rectangle """


class Rectangle:
    """ class attribtes"""
    number_of_instances = 0
    print_symbol = "#"

    """ instantiates an instance attributes """
    def __init__(self, width=0, height=0):
        """ initialization of attributes
        Args:
            width: represent the width of rectangle
            height: represent the height of this rectangle
        Raises:
            TypeError: if size is not integer
            VealueError: if value is less than o
         """
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    def __str__(self):
        result = ""
        if self.__width == 0 or self.__height == 0:
            return result
        for i in range(self.__height):
            for j in range(self.__width):
                result += str(self.print_symbol)
            if i < (self.__height - 1):
                result += '\n'
        return result

    def __repr__(self):
        return f"{type(self).__name__}({self.__width}, {self.__height})"

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

    def area(self):
        """ returns area of a rectangle """
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            perimeter = 0
        else:
            perimeter = 2 * (self.__height + self.__width)
        return perimeter

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        ''' returns a new Rectangle instance with equal size '''
        new_rect = cls(size, size)
        return new_rect

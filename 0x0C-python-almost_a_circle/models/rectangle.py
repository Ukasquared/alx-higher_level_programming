#!/usr/bin/python3
""" inherit the base module """


from models.base import Base


class Rectangle(Base):
    """ creates a rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize the instance attributes """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ gets the private attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the private attribute """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ gets the private attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the private attribute """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ gets the private attribute """
        return self.__x

    @x.setter
    def x(self, xvalue):
        """ sets the private attribute """
        if type(xvalue) is not int:
            raise TypeError("x must be an integer")
        if xvalue < 0:
            raise ValueError("x must be >= 0")
        self.__x = xvalue

    @property
    def y(self):
        """ gets the private attribute """
        return self.__y

    @y.setter
    def y(self, yvalue):
        """ sets the private attribute """
        if type(yvalue) is not int:
            raise TypeError("y must be an integer")
        if yvalue < 0:
            raise ValueError("y must be >= 0")
        self.__y = yvalue

    def area(self):
        """ compute the area, and return to user
        after validation """
        return self.__width * self.__height

    def display(self):
        """ display to the user """
        for i in range(self.y):
            print()
        letter = "#"
        for i in range(self.height):
            print("{}{}".format(" " * self.x, letter * self.width))

    def __str__(self):
        """ display to the user """
        return (f"[{type(self).__name__}] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """ replace the value with a new value and then
        validation """
        if args:
            attributes = ["id", "width", "height", "x", 'y']
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            if kwargs:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        return {
            'id': self.id,
            'width': self.width,
            'x': self.x,
            'height': self.height,
            'y': self.y
        }

#!/usr/bin/python3
"""
Contains class Rectangle
It inherits Base (check directory)
"""

from models.base import Base


class Rectangle(Base):
    """Inits rectangle instance"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization with id"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def check_value(self, name, value):
        """value checker"""

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if len(name) > 2:
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        else:
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """width getter"""
        return self.__width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @width.setter
    def width(self, value):
        self.check_value("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        self.check_value("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        self.check_value("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        self.check_value("y", value)
        self.__y = value

    def area(self):
        """returns area of rectangle"""
        return self.__height * self.__width

    def display(self):
        """Prints the rectangle using #"""
        [print("") for _ in range(self.y)]
        for _ in range(self.__height):
            print(" " * self.x, end="")
            print("#" * self.__width, end="\n")

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """updates rectangle using args"""
        expected = (self.id, self.width, self.height, self.x, self.y)

        # gets all args then appends whats
        # left over from already existing values

        if args:
            new_values = args + expected[len(args):len(expected)]
            self.id, self.width, self.height, self.x, self.y = new_values
        elif kwargs:
            for (name, value) in kwargs.items():
                setattr(self, name, value)

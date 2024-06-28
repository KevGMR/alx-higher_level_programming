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

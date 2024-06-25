#!/usr/bin/python3
"""Defines class Rectangle"""


class Rectangle:
    """class rectangle definitions"""
    def __init__(self, width=0, height=0):
        """init with height and width"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @width.setter
    def width(self, value):
        """setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """function to return area, it is public"""
        return self.__height * self.__width

    def perimeter(self):
        """function to return perimeter, it is public"""
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

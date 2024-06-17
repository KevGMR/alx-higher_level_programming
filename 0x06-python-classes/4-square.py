#!/usr/bin/python3
"""Defines Class Square"""


class Square:
    """Defines instance of class"""
    def __init__(self, size=0):
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """Getter to retrieve size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter to update size"""
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Returns area of square"""
        return self.__size * self.__size

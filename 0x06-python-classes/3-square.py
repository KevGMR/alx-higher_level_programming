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

    def area(self):
        return self.__size * self.__size

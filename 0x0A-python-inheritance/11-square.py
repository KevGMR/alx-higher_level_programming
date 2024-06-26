#!/usr/bin/python3
"""SQUARE DEF AND SUPER"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inits for square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)

        self.__size = size

    def __repr__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)

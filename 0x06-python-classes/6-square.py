#!/usr/bin/python3
"""Defines Class Square"""


class Square:
    """Defines instance of class"""
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getter to retrieve size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter to update size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Getter to retrieve position"""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple \
                             of two positive integers")
        self.__position = value

    def area(self):
        """Returns area of square"""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square"""
        if self.__size == 0:
            print("")
        else:
            for _ in range(0, self.__position[1]):
                print("")
            for _ in range(0, self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size, end="")
                print("")

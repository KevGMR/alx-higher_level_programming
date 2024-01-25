#!/usr/bin/python3
"""
Defines a square.

Attributes:
- size (int): The size of the square.
"""
class Square:
    """
    Initializes a new square instance.

    Parameters: 
    - size (int, optional): The size of the square (default is 0).
    """
    def __init__(self, size=0):

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = size
    """
    Calculates and returns the current square area.

    Returns:
    - int: The area of the square.
    """
    def area(self):

        return self.__size ** 2

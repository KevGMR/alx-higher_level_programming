#!/usr/bin/python3
"""
Defines a square.

Attributes:
    - size (int): The size of the square.
    - position (tuple): The position of the square.
"""
class Square:
    """
    Initializes a new square instance.

    Parameters:
    - size (int): The size of the square.
    - position (tuple): The position of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    """
    Getter method to retrieve the size of the square.

    Returns:
    - int: The size of the square.
    """
    @property
    def size(self):
        return self.__size

    """
    Setter method to set the size of the square.

    Parameters:
    - value (int): The new size of the square.

    Raises:
    - TypeError: If size is not an integer.
    - ValueError: If size is less than 0.
    """
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = value

    """
    Getter method to retriev the position of the square.

    Returns:
    - tuple: The position of the square.
    """
    @property
    def position(self):
        return self.__position

    """
    Setter method to set the position of the square.

    Parameters:
    - value (tuple): The new position of the square

    Raises:
    - TypeError: If the position is not a tuple of 2 positive integers.
    """
    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2 or type(value[0]) is not int \
                or type(value[1]) is not int or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of two positive integers")
        else:
            self.__position = value

    """
    Calculates and returns the current square area.

    Returns:
    - int: The area of the square.
    """
    def area(self):
        return self.__size ** 2

    """
    Prints the square with the character #.

    If size is equal to 0, print an empty line.
    Position is used by using space; lines are not filled with spaces when position[1] > 0.
    """
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

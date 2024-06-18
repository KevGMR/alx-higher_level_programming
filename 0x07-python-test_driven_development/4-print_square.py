#!/usr/bin/python3
"""
Function that prints square using #
"""


def print_square(size):
    """
    Function that prints square using #
    Return:
        Prints Square
    Raises:
        TypeError and ValueError
    """
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)

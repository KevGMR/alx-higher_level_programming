#!/usr/bin/python3
"""
Function that adds
two
integers
"""


def add_integer(a, b=98):
    """
        Function raises error if not int or \
        float converts floats to int if exceptions pass
    """
    if not isinstance(a, float) and not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, float) and not isinstance(b, int):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b

#!/usr/bin/python3
"""
Function to say my name
"""


def say_my_name(first_name, last_name=""):
    """
    Function for string concatenation
    """

    if not isinstance(first_name, str) or not first_name:
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str) or not len(last_name) >= 0:
        raise TypeError("last_name must be a string")

    print(f"{first_name} {last_name}")

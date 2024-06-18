#!/usr/bin/python3
"""
Function to say my name
"""


def say_my_name(first_name, last_name=""):
    """
    Function for string concatenation
    """

    if not isinstance(first_name, str) and not first_name:
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str) and not last_name:
        raise TypeError("last_name must be a string")

    print(f"{first_name} {last_name}")

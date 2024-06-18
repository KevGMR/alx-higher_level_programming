#!/usr/bin/python3
"""
Function to say my name
"""


def say_my_name(first_name, last_name=""):
    """
    Function for string concatenation
    Returns:
        No return
    Raises:
        TypeError: If first_name or last_name is not a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

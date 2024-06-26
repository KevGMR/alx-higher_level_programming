#!/usr/bin/python3
"""Definitions for class Recatangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Initializations for rectangle"""
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, 'height', height)
        self.__height = height
        BaseGeometry.integer_validator(self, 'width', width)
        self.__width = width

    def area(self):
        """returns area"""
        return self.__width * self.__height

    def __repr__(self):
        """returns class init in str"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

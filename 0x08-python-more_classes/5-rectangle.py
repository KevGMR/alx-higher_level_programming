#!/usr/bin/python3
"""
Class for rectangle
"""


class Rectangle:
    """functions within class rectangle"""
    def __init__(self, width=0, height=0):
        """init values for height and weight"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @width.setter
    def width(self, value):
        """setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """returns area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0

        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Print the rectangle using #"""
        if self.__height == 0 or self.__width == 0:
            return ""

        return ("\n".join("".join(["#" for _ in range(self.__width)])
                          for _ in range(self.__height)))

    def __repr__(self):
        """return a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """print message on instance deletion"""
        print("Bye rectangle...")

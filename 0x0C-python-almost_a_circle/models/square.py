#!/usr/bin/python3
"""
Contains Square that inherits from Class Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square Class inherits from Rectangle Class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """initialization"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for square size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        this updates using args and kwargs
        args
        order is id, size, x, y
        """
        expected = (self.id, self.size, self.x, self.y)

        new_tuple = args + expected[len(args):len(expected)]

        # print(expected)
        # print(new_tuple)
        if args:
            self.id, self.size, self.x, self.y = new_tuple
        elif kwargs:
            for (key, value) in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

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
        self.size = size

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.size)

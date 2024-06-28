#!/usr/bin/python3
"""
Contains tests for all models
"""

import unittest
from models.base import Base


class test_base_init(unittest.TestCase):
    """this tests the init of the Base Class"""

    def test_no_arg(self):
        """tests Base with no args"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        """tests Base with no args thrice, checks if id is valid"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b2.id - 1, b3.id - 2)


if __name__ == "__main__":
    unittest.main()

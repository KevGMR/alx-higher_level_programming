#!/usr/bin/python3
"""
Contains tests for all models,
checks if id is properly assigned at __init__
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """this tests the init of the Base Class"""

    def test_init(self):
        """tests base init"""
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)


if __name__ == "__main__":
    unittest.main()

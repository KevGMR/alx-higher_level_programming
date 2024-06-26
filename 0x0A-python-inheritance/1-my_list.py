#!/usr/bin/python3
"""Mylist inherits from list"""


class MyList(list):
    """inherists from list"""
    def print_sorted(self):
        """prints sorted  list"""

        print(sorted(self))

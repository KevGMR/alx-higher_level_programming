#!/usr/bin/python3
"""Defines func write file"""


def write_file(filename="", text=""):
    """the func that writes text to file"""
    with open(filename, "w", encoding='utf=8') as f:
        return f.write(text)

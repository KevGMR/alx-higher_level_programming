#!/usr/bin/python3
"""
Split Long Line
"""


def text_indentation(text):
    """
    Split Long Line
    Return
        list
    Raises
        TypeError
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    s = text[:]

    for d in ".?:":
        list_text = s.split(d)
        s = ""
        for i in list_text:
            i = i.strip(" ")
            s = i + d if s is "" else s + "\n\n" + i + d

    print(s[:-3], end="")

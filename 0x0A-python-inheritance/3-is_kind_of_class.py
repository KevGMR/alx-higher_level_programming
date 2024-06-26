#!/usr/bin/python3

def is_same_class(obj, a_class):
    """returns true if obj is class instance"""
    if isinstance(obj, a_class):
        return True
    else:
        return False

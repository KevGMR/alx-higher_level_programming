#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        fnc = fct(*args)
        return fnc
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None

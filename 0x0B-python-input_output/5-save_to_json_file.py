#!/usr/bin/python3
"""
Contains the save_to_json function
"""
import json


def save_to_json_file(my_obj, filename):
    """wites object to text file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)

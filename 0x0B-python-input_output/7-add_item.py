#!/usr/bin/python3
"""Program to save strings from command line arguments to file called
`add_item.json`. File contains a json serialized list of all strings
entered as arguments to the program.
"""
import sys
import json


if __name__ == "__main__":
    save_to_json_file = \
        __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    FILE_NAME = "add_item.json"
    with open(FILE_NAME, 'a+', encoding="utf-8") as f:
        # a+ creates the file if it doesnt exist, but it appends
        # Checks if file is empty
        # json.dump writes to file in this case []
        if f.tell() == 0:
            json.dump([], f)
    file_data = load_from_json_file("add_item.json")
    if len(sys.argv) > 1:
        file_data.extend(sys.argv[1:])
    save_to_json_file(file_data, FILE_NAME)

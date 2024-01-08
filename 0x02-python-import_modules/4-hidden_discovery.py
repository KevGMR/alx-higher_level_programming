#!/usr/bin/python3

# Import hidden_4
import hidden_4

# This code should not run when this file is imported
if __name__ == "__main__":

    # Iterate through list of defined names in module
    for def_name in dir(hidden_4):
        if def_name[:2] != "__":
            print(def_name)

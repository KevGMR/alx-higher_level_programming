#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    dict_keys = a_dictionary.keys()

    for i in dict_keys:
        value = a_dictionary.get(i)
        new_dict[i] = value * 2

    return new_dict

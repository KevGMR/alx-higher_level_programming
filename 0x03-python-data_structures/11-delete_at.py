#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = []

    for index, i in enumerate(my_list):
        if index != idx:
            new_list.append(i)

    return new_list

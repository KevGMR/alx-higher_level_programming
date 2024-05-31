#!/usr/bin/python3


def new_in_list(my_list, index, element):

    if (index < 0) or (index > (len(my_list)-1)):
        return my_list

    copy = [x for x in my_list]
    copy[index] = element
    return copy

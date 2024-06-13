#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    idx_1 = 0
    idx_2 = 0
    for index, i in enumerate(tuple_a):
        if index == 0:
            idx_1 += i
        if index == 1:
            idx_2 += i
    for index2, j in enumerate(tuple_b):
        if index2 == 0:
            idx_1 += j
        if index2 == 1:
            idx_2 += j
    return tuple((idx_1, idx_2))

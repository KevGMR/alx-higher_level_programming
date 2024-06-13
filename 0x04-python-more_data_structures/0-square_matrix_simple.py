#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        inner_matrix = []
        for j in i:
            inner_matrix.append(j*j)
        new_matrix.append(inner_matrix)

    return new_matrix

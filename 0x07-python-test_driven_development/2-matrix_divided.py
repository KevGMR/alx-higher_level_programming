#!/usr/bin/python3
"""
Function that divides all in matrix
"""


def matrix_divided(matrix, div):
    """
    Function that divides all in matrix
    """

    error = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix:
        raise TypeError(error)
    if not isinstance(matrix, list):
        raise TypeError(error)
    if not isinstance(div, float) and not isinstance(div, int):
        raise TypeError("div must be a number")

    result = []
    matrix_len = len(matrix[0])

    for i in matrix:
        if len(i) > matrix_len:
            raise TypeError("Each row of the matrix must have the same size")

        inner_result = []
        for j in i:
            if not isinstance(j, float) and not isinstance(j, int):
                raise TypeError(error)
            if j == 0:
                raise ZeroDivisionError("division by zero")

            inner_result.append(round(j / div, 2))
        result.append(inner_result)

    return result

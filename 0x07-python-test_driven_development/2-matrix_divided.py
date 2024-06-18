#!/usr/bin/python3

def matrix_divided(matrix, div):
    result = []

    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, float) and not isinstance(div, int):
        raise TypeError("div must be a number")
    for i in matrix:
        inner_result = []
        for j in i:
            if not isinstance(j, float) and not isinstance(j, int):
                raise TypeError("matrix must be a matrix (list of lists) of"
                                " integers/floats")
            if j == 0:
                raise ZeroDivisionError("division by zero")

            inner_result.append(float("{:.2f}".format(j/div)))
        result.append(inner_result)

    return result

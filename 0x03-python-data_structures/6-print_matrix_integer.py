#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for index, column in enumerate(row):
            if (index < len(row) - 1):
                print(column, end=" ")
            else:
                print(column, end="")
        print("", end="\n")

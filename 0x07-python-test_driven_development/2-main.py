#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [[1, 2, 3], [4, 5, 6]]
noneL = None
empty_list = []
empty_lists = [[], [], []]
not_list = [42, [2, 5], [1, 2, 3]]
not_all_num = [["blue", 1, 2], [3, 4, "f"], ["23b", 5, 6]]
diff_len = [[1, 3, 3, 3], [3, 5, 1, 2, 5], [2, 5, 8]]

print(matrix_divided(matrix, 3))
print(matrix)
print(matrix_divided(noneL, 3))
print(matrix_divided(empty_list, 2))
print(matrix_divided(empty_lists, 3))

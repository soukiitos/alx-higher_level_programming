#!/usr/bin/python3
a = '6-print_matrix_integer'
print_matrix_integer = __import__(a).print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()

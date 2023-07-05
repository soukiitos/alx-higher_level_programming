#!/usr/bin/python3
def matrix_divided(matrix, div):
    Err_Msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix or not isinstance(matrix, list) or any(
            not isinstance(lsts, list) for lsts in matrix):
        raise TypeError(Err_Msg)
    if any(not isinstance(item, (int, float)) for lsts in matrix
            for item in lsts):
        raise TypeError(Err_Msg)
    if any(len(lsts) == 0 for lsts in matrix):
        raise TypeError(Err_Msg)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not all(len(lsts) == len(matrix[0]) for lsts in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in lsts] for lsts in matrix]

#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqr = []
    for i in matrix:
        sqr.append([j**2 for j in i])
    return(sqr)

#!/usr/bin/python3
'''Define a pascal_triangle function'''


def pascal_triangle(n):
    '''Return a list of lists of integers
    representing the Pascal’s triangle of n'''
    if n <= 0:
        return []
    t = []
    for i in range(n):
        for j in range(i + 1):
            if j == 0:
                t.append([1])
            elif j == i:
                t[i].append(1)
            else:
                t[i].append(t[i - 1][j] + t[i - 1][j - 1])
    return t

#!/usr/bin/python3
# 4-print_square.py
'''Define a square-printing function'''


def print_square(size):
    ''''Print a square with the charcter #'''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")

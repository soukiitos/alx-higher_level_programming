#!/usr/bin/python3
# 0-add_integer.py
'''Define The addition of 2 integers'''


def add_integer(a, b=98):
    '''Add 2 integers'''
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

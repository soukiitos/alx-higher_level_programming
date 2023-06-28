#!/usr/bin/python3
'''Define a square'''


class Square:
    '''Initialise the data'''
    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

#!/usr/bin/python3
'''Define a square'''


class Square:
    '''Initialise the data'''
    def __init__(self, size=0):
        self.__size = size
    '''Return the current square area'''
    def area(self):
        return self.__size**2
    '''Get method'''
    @property
    def size(self):
        return self.__size
    '''set method'''
    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
    '''Compare squres'''
    def __It__(self, other):
        return self.area() < other.area()
    '''Compare squares'''
    def __le__(self, other):
        return self.area() <= other.area()
    '''Compare squares'''
    def __eq__(self, other):
        return self.area() == other.area()
    '''Compare squares'''
    def __ne__(self, other):
        return self.area() != other.area()
    '''Compare squares'''
    def __gt__(self, other):
        return self.area() > other.area()
    '''Compare squares'''
    def __ge__(self, other):
        return self.area() >= other.area()

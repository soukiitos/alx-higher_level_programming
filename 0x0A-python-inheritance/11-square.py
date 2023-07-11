#!/usr/bin/python3
'''Define a class Square that inherits from Rectangle'''
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    '''A square class'''
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
    '''Return the area of the square'''
    def area(self):
        return self.__size ** 2
    '''Return the string'''
    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))

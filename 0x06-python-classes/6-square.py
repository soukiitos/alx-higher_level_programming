#!/usr/bin/python3
'''Define a square'''


class Square:
    '''Initialise the data'''
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position
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
    '''Print in stdout the square with the character #'''
    def my_print(self):
        if self.__size != 0:
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(' ', end='')
                for j in range(self.__size):
                    print('#', end='')
                print()
        else:
            print()
    '''Get method'''
    @property
    def position(self):
        return self.__position
    '''Set method'''
    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(i) != int for i in value) or any(j < 0 for j in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

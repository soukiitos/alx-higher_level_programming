#!/usr/bin/python3
import math
'''MagicClass using some magic methods'''


class MagicClass:
    '''initialize an instance of the class'''
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius
    '''Calculate the area'''
    def area(self):
        return self.__radius**2 * math.pi
    '''Claculate the circumference'''
    def circumference(self):
        return 2*math.pi * self.__radius

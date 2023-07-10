#!/usr/bin/python3
'''Define an empty class BaseGeometry'''


class BaseGeometry:
    '''Geometry module BaseGeometry'''

    def area(self):
        '''Raise an Exception'''

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Validate the value'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

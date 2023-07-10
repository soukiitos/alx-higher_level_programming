#!/usr/bin/python3
'''Define a class Rectangle that inherits from BaseGeometry'''
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''A Rectangle class'''

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
    '''Return the area of the rectangle'''
    def area(self):
        return self.__width * self.__height
    '''Return the string'''
    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

#!/usr/bin/python3
'''Define a rectangle'''


class Rectangle:
    '''Instantiation with optional width and height'''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''Create instantiation of rectangle
        Args:
        width (int): The width of thhe rectangle.
        height (int): The height of the rectangle.
        '''
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    '''width getter'''
    @property
    def width(self):
        return self.__width

    '''width setter'''
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    '''height getter'''
    @property
    def height(self):
        return self.__height

    '''height setter'''
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    '''Return the rectangle area'''
    def area(self):
        return self.__width * self.__height

    '''Return the rectangle perimeter'''
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    '''Print the rectangle with the character #'''
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = []
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append(str(self.print_symbol))
            rectangle.append("\n")
        rectangle.pop()
        return "".join(rectangle)

    '''Recreate a new instance'''
    def __repr__(self):
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    '''Delete an instance'''
    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    '''Compare rectangles'''
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise ValueError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

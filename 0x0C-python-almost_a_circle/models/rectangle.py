#!/usr/bin/python3
'''Define a rectangle class'''
from models.base import Base


class Rectangle(Base):
    '''Define the class constractor init file'''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    '''Define the width of the rectangle'''
    @property
    def width(self):
        return self.__width

    '''Defie the set of the width of the rectangle'''
    @width.settter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    '''Define the height of the rectangle'''
    @property
    def height(self):
        return self.__height

    '''Define the set of the height of the rectangle'''
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    '''Define the x of the rectangle'''
    @property
    def x(self):
        return self.__x

    '''Define the set of the x of the rectangle'''
    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    '''Define the y of the rectangle'''
    @property
    def y(self):
        return self.__y

    '''Define the set of the y of the rectangle'''
    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    '''Return the area value of the Rectangle instance'''
    def area(self):
        return self.width * self.height

    '''Print n stdout the Rectangle instance with the character #'''
    def display(self):
        for i in range(self.y):
            print()
        for j in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for w in range(self.width):
                print("#", end="")
            print()

    '''Define the str of the rectangle'''
    def __str__(self):
        return "[{}] ({}) {}/{} - {}/{}".\
                format(
                        type(self).__name__,
                        self.id,
                        self.x,
                        self.y,
                        self.width,
                        self.height
                        )

    '''Define the update of the rectangle'''
    def update(self, *args, **kwargs):
        if args:
            self.id = args[0] if len(args) >= 1 else None
            self.width = args[1] if len(args) >= 2 else self.width
            self.height = args[2] if len(args) >= 3 else self.height
            self.x = args[3] if len(args) >= 4 else self.x
            self.y = args[4] if len(args) >= 5 else self.y
        elif kwargs:
            self.id = kwargs.get('id', self.id)
            self.width = kwargs.get('width', self.width)
            self.height = kwargs.get('height', self.height)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)

    '''Define the dictionary of the rectangle'''
    def to_dictionary(self):
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }

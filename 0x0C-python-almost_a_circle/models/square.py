#!/usr/bin/python3
'''Define a square class'''
from models.rectangle import Rectangle


class square:
    '''Define the class constractor init file'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    '''Define the string file'''
    def __str__(self):
        return "[{}] ({}) {}/{} - {}".\
                format(
                        type(self).__name__,
                        self.id,
                        self.x,
                        self.y,
                        self.width
                        )

    @property
    '''Define the square size'''
    def size(self):
        return self.width

    @size.setter
    '''Define the square size'''
    def size(self, value):
        self.width = value
        self.height = value

    '''Define the square update'''
    def update(self, *args, **kwargs):
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    '''Define the dictionary representation of a rectangle'''
    def to_dictionary(self):
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }

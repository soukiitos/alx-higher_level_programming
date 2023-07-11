#!/usr/bin/python3
'''Define a student class'''


class Student():
    '''Define a student'''
    def __init__(self, first_name, last_name, age):
        '''Drfine a student function by instance attributes:
        first_name, last_name and age'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    '''Retrieve a dictionary representation of a Student instance'''
    def to_json(self, attrs=None):
        if attrs is not None:
            return {i: j for i, j in self.__dict__.items() if i in attrs}
        return self.__dict__

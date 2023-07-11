#!/usr/bin/python3
'''Define a class MyInt that inherits from int'''


class MyInt(int):
    '''Inverted operators'''
    def __eq__(self, value):
        return int(self) != int(value)
    '''Overide != operator and inverts != operator'''
    def __ne__(self, value):
        return self.real == value

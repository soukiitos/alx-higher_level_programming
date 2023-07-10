#!/usr/bin/python3
'''Define the same class or inherit from'''


def is_kind_of_class(obj, a_class):
    '''Return True if the object is an instance of,
    or if the object is an instance of a class
    that inherited from the specified class,
    Otherwise False'''

    return isinstance(obj, a_class)

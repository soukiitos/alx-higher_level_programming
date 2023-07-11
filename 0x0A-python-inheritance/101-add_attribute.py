#!/usr/bin/python3
'''Add a new attribute to an object if it’s possible'''


def add_attribute(obj, att, value):
    '''add a new attribute'''
    if hasattr(obj, "__dict__") or \
            (hasattr(obj, "__slots__") and att in obj.__slots__):
        setattr(obj, att, value)
    else:
        raise TypeError("can't add new attribute")

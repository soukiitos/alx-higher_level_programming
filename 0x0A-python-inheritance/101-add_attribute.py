#!/usr/bin/python3
'''Add a new attribute to an object if it’s possible'''


def add_attribute(obj, att_name, value):
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att_name, value)

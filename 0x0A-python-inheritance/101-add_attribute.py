#!/usr/bin/python3
'''Add a new attribute to an object if it’s possible'''


def add_attribute(obj, att_name, value):
    if hasattr(obj, "__dict__") or \
            (hasattr(obj, "__slots__") and att_name in obj.__slots__):
        setattr(obj, att_name, value)
    else:
        raise TypeError("can't add new attribute")

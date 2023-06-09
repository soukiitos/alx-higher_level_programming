#!/usr/bin/python3
'''Define Only sub class of a class that inherited'''


def inherits_from(obj, a_class):
    '''Return True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class;
    Otherwise False'''

    return isinstance(obj, a_class) and type(obj) != a_class

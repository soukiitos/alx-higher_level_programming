#!/usr/bin/python3
'''Return a string “BestSchool” n times the number of the iteration'''
def magic_string():
    magic_string.a = getattr(magic_string, 'a', 0) + 1
    return("BestSchool, " * (magic_string.a - 1) + "BestSchool")

#!/usr/bin/python3
'''Define an append_write function'''


def append_write(filename="", text=""):
    '''Append a string at the end of a text file (UTF8)
    and returns the number of characters added'''
    with open(filename, 'a') as f:
        return f.write(text)

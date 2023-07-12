#!/usr/bin/python3
'''Define an append_after function'''


def append_after(filename="", search_string="", new_string=""):
    '''Insert a line of text to a file,
    after each line containing a specific string'''
    a = "" '''initialize as an empty string'''
    with open(filename, 'r') as f:
        for i in f:
            a += i
            if search_string in i:
                a += new_string
    with open(filename, 'w') as f:
        f.write(a)

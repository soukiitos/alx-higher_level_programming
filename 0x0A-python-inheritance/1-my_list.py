#!/usr/bin/python3
'''Define a MyList class'''


class MyList(list):
    '''class MyList that inherits from list'''

    def print_sorted(self):
        '''Print the list, but sorted'''

        print(sorted(self))

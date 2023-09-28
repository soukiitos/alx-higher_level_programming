#!/usr/bin/python3
'''Find a peak in a list of unsorted integers'''


def find_peak(list_of_integers):
    '''Define a find peak'''
    if not list_of_integers:
        return None

    i, j = 0, len(list_of_integers) - 1

    while (i < j):
        middle = (i + j) // 2
        if list_of_integers[middle] > list_of_integers[middle + 1]:
            j = middle
        else:
            i = middle + 1
    return list_of_integers[i]

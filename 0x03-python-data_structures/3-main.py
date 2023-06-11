#!/usr/bin/python3
a = '3-print_reversed_list_integer'
print_reversed_list_integer = __import__(a).print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)

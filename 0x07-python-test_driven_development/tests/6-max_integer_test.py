#!/usr/bin/python3
# 6-max_integer_test.py
import unittest
'''Define test_max_integer class'''


class TestMaxInteger(unittest.TestCase):
    '''Define an ordered list'''

    def test_ordered_list(self):
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)
    '''Define an unordered list'''

    def test_unordered_list(self):
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)
    '''Define the max value'''

    def test_max_at_begginning(self):
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_begginning), 4)
    '''Define an empty list'''

    def test_empty_list(self):
        empty = []
        self.assertEqual(max_integer(one_element), 7)
    '''Define a list with a single element'''

    def test_one_element_list(self):
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)
    '''Define a list of floats'''

    def test_floats(self):
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)
    '''Define a list of ints and floats'''

    def test_ints_and_floats(self):
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)
    '''Define a string'''

    def test_string(self):
        string = "Brennan"
        self.assertEqual(max_integer(string), 'r')
    '''Define a list of strings'''

    def test_list_of_strings(self):
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")
    '''Define an empty string'''

    def test_empty_string(self):
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()

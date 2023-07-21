#!/usr/bin/python3
'''Define unittest for BaseTest'''


import unittest
import os
import json
import pep8
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


'''Define BaseTest Class'''
class BaseTest(unittest.TestCase):
    '''Import module'''
    def setUp(self):
        Base._Base__nb_objects = 0
        pass
    '''Clean after each test'''
    self.assertTrue(hasattr(Base, '_Base__nb_objects'), 0)
    '''Defining unittest for testing instantiation'''
    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)
    '''Defining unittest for testing three bases'''
    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b2.id - 2)
    '''Defining unittest for id'''
    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)
    '''Defining unittest of unique id'''
    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)
    '''Defining unittest of after unique id'''
    def
if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
'''Define unittest for BaseTest'''


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    '''Define the setUp'''
    def setUp(self):
        Base._Base__nb_objects = 0
        pass

    '''Define  tearDown function'''
    def tearDown(self):
        pass

    '''Define a nb_objects test'''
    def test_nb_objects(self):
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    '''Define the initialize of nb_objects'''
    def test_nb_oobjects_initialized(self):
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    '''Define the instantiation'''
    def test_instantiation_c(self):
        b = Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b.__dict__, {"id": 1})
        self.assertEqual(b.id, 1)

    '''Define the constructor'''
    def test_constructor_D(self):
        with self.assertRaises(TypeError) as e:
            Base.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    '''Define the constructor'''
    def test_constructor_args(self):
        with self.assertRaises(TypeError) as e:
            Base.__init__(self, 1, 2)
        msg = "
        __init__() takes from 1 to 2 positional arguments but 3 were given
        "
        self.assertEqual(str(e.exception), msg)

    '''Define the consecutive'''
    def test_consecutive(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    '''Define the sync'''
    def test_sync(self):
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    '''Define more sync'''
    def test_more_sync(self):
        b = Base()
        b = Base("Foo")
        b = Base(98)
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    '''Define the integer id'''
    def test_custom_id_int(self):
        i = 98
        b = Base(i)
        self.assertEqual(b.id, i)

    '''Define the str id'''
    def test_custom_id_str(self):
        i = "FooBar"
        b = Base(i)
        self.assertEqual(b.id, i)

    '''Define the keyword'''
    def test_keyword_id(self):
        i = 421
        b = Base(id=i)
        self.assertEqual(b.id, i)

    '''Define the json_string'''
    def test_json_string_H(self):
        with self.assertRaises(TypeError) as e:
            Base.to_json_string()
        s = "to_json_string() missing 1 required positional argument:
            'list_dictionaries'"
        self.assertEqual(str(e.exception), s)
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        d = [{
            'x': 101,
            'y': 20123,
            'width': 312321,
            'id': 522244,
            'height': 34340
            }]
        self.assertEqual(
                len(Base.to_json_string(d)),
                len(str(d))
                )
        d = [{
            'x': 1,
            'y': 2,
            'width': 3,
            'id': 4,
            'height': 5
            }]
        self.assertEqual(
                len(Base.to_json_string(d)),
                len(str(d))
                )
        d = [{"foobarrooo": 989898}]
        self.assertEqual(
                Base.to_json_string(d),
                '[{"foobarrooo": 989898}]'
                )
        d = [
                {"foobarrooo": 989898},
                {"abc": 123},
                {"HI": 0}
                ]
        self.assertEqual(
                Base.to_json_string(d),
                '[{"foobarrooo": 989898}, {"abc": 123}, {"HI": 0}]'
                )
        d = [
                {'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5},
                {
                    'x': 101, 'y': 20123,
                    'width': 312321, 'id': 522244, 'height': 34340
                    }
                ]
        self.assertEqual(len(Base.to_json_string(d)), len(str(d)))
        d = [{}]
        self.assertEqual(Base.to_json_string(d), '[{}]')
        d = [{}, {}]
        self.assertEqual(Base.to_json_string(d), '[{}, {}]')
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        dictionary = str([dictionary])
        dictionary = doctionary.repalce("'", '"')
        self.assertEqual(dictionary, json_dictionary)
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(1, 2, 3, 4)
        r3 = Rectangle(2, 3, 4, 5)
        dictionary = [
                r1.to_dictionary(),
                r2.to_dictionary(),
                r3.to_dictionary()
                ]
        json_dictionary = Base.to_json_string(dictionary)
        dictionary = str(dictionary)
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)
        r1 = Square(10, 7, 2)
        r2 = Square(1, 2, 3)
        r3 = Square(2, 3, 4)
        dictionary = [
                r1.to_dictionary(),
                r2.to_dictionary(),
                r3.to_dictionary()
                ]
        json_dictionary = Base.to_json_string(dictionary)
        dictionary = str(dictionary)
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

    '''Define the to jason string test'''
    def test_H_from_json_string(self):
        with self.assertRaises(TypeError) as e:
            Base.from_json_string()
        s = "from_json_string() missing 1 required positional argument:
            'json_string'"
        self.assertEqual(str(e.exception), s)
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        s = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5},\
                {"x": 101, "y": 20123, "width": 312321, "id": 522244, \
                "height": 34340}]'
        d = [
                {'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5},
                {
                    'x': 101, 'y': 20123,
                    'width': 312321, 'id': 522244,
                    'height': 34340
                    }
                ]
        self.assertEqual(Base.from_json_string(s), d)
        d = [{}, {}]
        s = '[{}, {}]'
        self.assertEqual(Base.from_json_string(s), d)
        d = [{}]
        s = '[{}]'
        self.assertEqual(Base.from_json_string(s), d)
        d = [{"foobarrooo": 989898}, {"abc": 123}, {"HI": 0}]
        s = '[{"foobarrooo": 989898}, {"abc": 123}, {"HI": 0}]'
        self.assertEqual(Base.from_json_string(s), d)
        d = [{"foobarrooo": 989898}]
        s = '[{"foobarrooo": 989898}]'
        self.assertEqual(Base.from_json_string(s), d)
        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]
        s = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}]'
        self.assertEqual(Base.from_json_string(s), d)
        d = [
                {
                    'x': 101, 'y': 20123,
                    'width': 312321, 'id': 522244,
                    'height': 34340
                    }
                ]
        s = '[{"x": 101, "y": 20123, "width": 312321, \
                "id": 522244, "height": 34340}]'
        self.assertEqual(Base.from_json_string(s), d)
        list_in = [
                {'id': 89, 'width': 10, 'height': 4},
                {'id': 7, 'width': 1, 'height': 7}
                ]
        list_out = Rectangle.from_json_string(
                Rectangle.to_json_string(list_in)
                )
        self.assertEqual(list_in, list_out)

    '''Define save to file'''
    def test_save_to_file(self):
        import os
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 105)
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        try:
            os.remove("Rectangle.json")
        except TypeError:
            pass
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 52)
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        try:
            os.remove("Square.json")
        except TypeError:
            pass
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        r2 = Square(1)
        Square.save_to_file([r2])
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 38)

    '''Define the create method'''
    def test_J_create(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    '''Define the loading from file'''
    def test_load_from_file_F(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_in = [r1, r2]
        Rectangle.save_to_file(list_in)
        list_out = Rectangle.load_from_file()
        self.assertNotEqual(id(list_in[0]), id(list_out[0]))
        self.assertEqual(str(list_in[0]), str(list_out[0]))
        self.assertNotEqual(id(list_in[1]), id(list_out[1]))
        self.assertEqual(str(list_in[1]), str(list_out[1]))
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_in = [s1, s2]
        Square.save_to_file(list_in)
        list_out = Square.load_from_file()
        self.assertNotEqual(id(list_in[0]), id(list_out[0]))
        self.assertEqual(str(list_in[0]), str(list_out[0]))
        self.assertNotEqual(id(list_in[1]), id(list_out[1]))
        self.assertEqual(str(list_in[1]), str(list_out[1]))


if __name__ == "__main__":
    unittest.main()

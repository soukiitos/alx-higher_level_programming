#!/usr/bin/python3
'''Define a base class model'''
import csv
import json
from json import loads, dumps
import turtle
import time
from random import randrange
from os import path
from models.rectangle import Rectangle
from models.square import Square


class Base:
    '''Base class'''
    __nb_objects = 0
    '''Define a init file'''
    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    '''Define json list of dictionary'''
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    '''Define json string'''
    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "[]":
            return []
        return loads(json_string)

    '''Define the saves of json to file'''
    @classmethod
    def save_to_file(cls, list_objs):
        with open("{}.json".format(cls.__name__), "w") as f:
            f.write(cls.to_json_string(list_objs))
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        else:
            f.write("[]")

    '''Define a create file'''
    @classmethod
    def create(cls, **dictionary):
        if cls is Rectangle:
            new = cls(1, 1)
        elif cls is Square:
            new = cls(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    '''Define a string loading file'''
    @classmethod
    def load_from_file(cls):
        try:
            with open("{}.json".format(cls.__name__), "r") as f:
                return [
                        cls.create(**d)
                        for d in cls.from_json_string(f.read())
                        ]
        except IOError:
            return []

    '''Define a csv save to file'''
    @classmethod
    def save_to_file_csv(cls, list_objs):
        if list_objs is not None:
            if cls is not Rectangle:
                list_objs = [[o.id, o.size, o.x, o.y] for o in list_objs]
            else:
                list_objs = [
                        [o.id, o.width, o.height, o.x, o.y]
                        for o in list_objs
                        ]
        with open('{}.csv'.format(cls.__name__), "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(list_objs)

    '''Define the csv load from file'''
    @classmethod
    def load_from_file_csv(cls):
        a = []
        filename = "{}.csv".format(cls.__name__)
        with open(filename, "r", newline="") as f:
            reader = csv.reader(f)
            for i in reader:
                i = [int(r) for r in i]
                if cls is not Rectangle:
                    d = {"id": i[0], "size": i[1], "x": i[2], "y": i[3]}
                else:
                    d = {
                            "id": i[0],
                            "width": i[1],
                            "height": i[2],
                            "x": i[3],
                            "y": i[4]
                            }
                a.append(cls.create(**d))
        return a

    '''Define a Rectangle and a Square drawing'''
    @staticmethod
    def draw(list_rectangles, list_squares):
        t = turtle.Turtle()
        t.screen.bgcolor("#a5fe67")
        t.pensize(3)
        t.shape("turtle")
        t.color("#ffafcf")
        for i in list_rectangles:
            t.showturtle()
            t.up()
            t.goto(i.x, i.y)
            t.down()
            for j in range(2):
                t.forward(i.width)
                t.left(90)
                t.forward(i.height)
                t.left(90)
            t.hideturtle()
        t.color("#d8ae7f")
        for q in list_squares:
            t.showturtle()
            t.up()
            t.goto(q.x, q.y)
            t.down()
            for qj in range(2):
                t.forward(q.width)
                t.left(90)
                t.forward(q.height)
                t.left(90)
            t.hideturtle()
        t.exitonclick()

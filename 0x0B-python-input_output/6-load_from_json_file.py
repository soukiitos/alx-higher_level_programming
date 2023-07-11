#!/usr/bin/python3
'''Define load_from_json_file function'''
import json


def load_from_json_file(filename):
    '''Create an Object from a “JSON file”'''
    with open(filename, 'r') as f:
        return json.load(f)

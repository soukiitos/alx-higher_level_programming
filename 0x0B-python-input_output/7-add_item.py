#!/usr/bin/python3
'''Define Load, add, save functions'''
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
if __name__ == "__main__":
    try:
        j_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        j_list = []

    for i in range(1, len(sys.argv)):
        j_list.append(sys.argv[i])
    save_to_json_file(j_list, "add_item.json")

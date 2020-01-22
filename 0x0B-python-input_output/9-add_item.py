#!/usr/bin/python3
""" This module adds all arguments to a Python list,
    and then save them to a file:
"""
import sys
import os

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"
if not os.path.exists(filename):
    a_list = []
    save_to_json_file(a_list, filename)
else:
    json_file = load_from_json_file(filename)
    if type(json_file) is list or type(json_file) is dict:
        for item in range(1, len(sys.argv)):
            json_file.append(sys.argv[item])
        save_to_json_file(json_file, filename)

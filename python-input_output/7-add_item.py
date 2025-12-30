#!/usr/bin/python3
"""
Adds all command-line arguments to a Python list
and saves it to a JSON file.
"""
import sys

save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

items = load('add_item.json')

for arg in sys.argv[1:]:
    items.append(arg)

save(items, 'add_item.json')


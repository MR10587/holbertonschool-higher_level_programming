#!/usr/bin/python3
import sys
import json
"""Salam"""


save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


load('add_item.json')

text = []
for arg in sys.argv[1:]:
    text.append(arg)

save(text, 'add_item.json')

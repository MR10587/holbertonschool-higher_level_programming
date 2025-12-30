#!/usr/bin/python3
"""Salam"""
import sys

save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    items = []
    items = load('add_item.json')
    items.extend(sys.argv[1:])
    save(items, 'add_item.json')

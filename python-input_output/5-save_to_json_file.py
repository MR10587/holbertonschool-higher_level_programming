#!/usr/bin/python3
"""Salam"""


import json


def save_to_json_file(my_obj, filename):
    """Sagol"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
        return f

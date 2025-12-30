#!/usr/bin/python3
"""Salam"""


import json


def load_from_json_file(filename):
    """Sagol"""
    with open(filename, 'a', encoding='utf-8') as f:
        for line in f:
            filename.write(json.loads(line))
            
        return filename

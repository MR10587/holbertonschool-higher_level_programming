#!/usr/bin/python3
"""Salam"""


import json


def load_from_json_file(filename):
    """Sagol"""
    with open(filename, 'w', encoding='utf-8') as f:
        return json.load(filename)

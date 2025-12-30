#!/usr/bin/python3
"""Salam"""


import json


def save_to_json_file(my_obj, filename):
    """Sagol"""
    filename = json.dumps(my_obj)
    return filename

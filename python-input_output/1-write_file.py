#!/usr/bin/python3
"""Writing File"""


def write_file(filename="", text=""):
    """Writing Text"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
        return f.tell()

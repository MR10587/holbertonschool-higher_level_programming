#!/usr/bin/python3
"""Writing File"""


def write_file(filename="", text=""):
    """Writing Text"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)

    total = 0
    for char in filename:
        total += 1
    return total

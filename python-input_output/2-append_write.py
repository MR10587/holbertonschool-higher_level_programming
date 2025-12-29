#!/usr/bin/python3
"""Append"""


def append_write(filename="", text=""):
    """Function"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
        return len(text)

#!/usr/bin/python3
"""First I/O project"""


def read_file(filename=""):
    """Reading File"""
    with open(filename, encoding="utf-8") as f:
        f.read()

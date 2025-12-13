#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        fct()
        return fct
    except ZeroDivisionError as a:
        print('Exception: {}'.format(a), file=sys.stderr)
        return None

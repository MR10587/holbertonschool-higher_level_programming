#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as a:
        return False
        print('Exception: {}'.format(a), file=sys.stderr)
        

#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""


class MyList(list):
    def print_sorted(self):
        print(sorted(self))

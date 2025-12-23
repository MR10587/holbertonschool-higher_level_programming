#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""


def is_same_class(obj, a_class):
    '''python3 -c 'print(__import__("my_module").my_function.__doc__)'
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    '''
    if type(obj).__name__ == a_class:
        return True
    return False

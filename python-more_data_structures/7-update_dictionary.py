#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary and value != a_dictionary[key]:
        a_dictionary[key] = value
    elif key not in a_dictionary:
        a_dictionary[key] = value

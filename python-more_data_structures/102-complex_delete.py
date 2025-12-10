#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    b_dictionary = {}
    for i in a_dictionary:
        if a_dictionary[i] != value:
            b_dictionary[i] = a_dictionary[i]
    a_dictionary = b_dictionary
    print(b_dictionary)

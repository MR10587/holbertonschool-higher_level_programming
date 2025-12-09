#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a = []
    for i in a_dictionary:
        a.append(f'{i}: {a_dictionary[i]}')
    b = sorted(a)
    for i in b:
        print(i)

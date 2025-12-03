#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in my_list:
        while type(my_list[i]) == str:
            if type(i) is int:
                print('{:d}'.format(i))

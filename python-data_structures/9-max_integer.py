#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) != 0:
        first = my_list[0]
        for i in my_list:
            if i > first:
                first = i
        return first
    else:
        return None

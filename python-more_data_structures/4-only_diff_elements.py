#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_12 = set_1 - set_2
    set_21 = set_2 - set_1
    set_3 = set_12 | set_21
    return set_3

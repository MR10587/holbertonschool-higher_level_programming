#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i in range(0, x):
        try:
            print(my_list[i], end='')
        except:
            print()
            return i
            break
    print()
safe_print_list([1,2,3,4], len(my_list))

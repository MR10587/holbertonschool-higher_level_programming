#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for index, j in enumerate(i):
            if index != 0:
                print(' ', end='')
            print('{:d}'.format(j), end='')
        print()

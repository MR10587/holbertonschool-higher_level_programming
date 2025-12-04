#!/usr/bin/python3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for index, j in enumerate(i):
            if index != 0:
                print(' ', end='')  # print space before elements except first
            print('{:d}'.format(j), end='')
        print()  # newline after each row

        
 
#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        arr = []
        for j in matrix[i]:
            j = j**2
            arr.append(j)
        new_matrix.append(arr)
    return new_matrix

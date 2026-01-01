#!/usr/bin/python3
"""MeeTion"""


def pascal_triangle(n):
    """HP"""
    lists = [[1], [1, 1]]
    if n == 0:
        return []
    if n == 1:
        return [[1]]
    elif n == 2:
        return lists
    for i in range(2, n):
        new_list = []
        new_list.append(1)
        prev = lists[-1]
        for k in range(1, len(prev)):
            new_list.append(prev[k-1] + prev[k])
        new_list.append(1)
        lists.append(new_list)

    return lists

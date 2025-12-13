#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(0, 3):
        try:
            if i > a:
                print('Exception: Too far')
            result += a**b / i
        except (TypeError, ValueError, ZeroDivisionError):
            result = a + b
            break
    return result

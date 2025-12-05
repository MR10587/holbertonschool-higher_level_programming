#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    else:
        operator = sys.argv[2]
        a: int = int(sys.argv[1])
        b: int = int(sys.argv[3])
        if operator == '+':
            result = add(a, b)
            print('{:d} {} {:d} = {:d}'.format(a, operator, b, result))
        elif operator == '-':
            result = sub(a, b)
            print('{:d} {} {:d} = {:d}'.format(a, operator, b, result))
        elif operator == '*':
            result = mul(a, b)
            print('{:d} {} {:d} = {:d}'.format(a, operator, b, result))
        elif operator == '/':
            result = div(a, b)
            print('{:d} {} {:d} = {:d}'.format(a, operator, b, result))
        else:
            print('Unknown operator. Available operators: +, -, * and /')

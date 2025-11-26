#!/usr/bin/python3
for i in range(100):
    if i >= 0 and i <= 9:
        print(f"0{i}", end=", ")
    elif i == 99:
        print(i)
    else:
        print(i, end=", ")

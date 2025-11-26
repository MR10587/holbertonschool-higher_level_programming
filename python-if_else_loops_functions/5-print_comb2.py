#!/usr/bin/python3
for i in range(100):
    if i >= 0 and i <= 9:
        print(f"0{i}", end=", ")
    else:
        print(i, end=", ")

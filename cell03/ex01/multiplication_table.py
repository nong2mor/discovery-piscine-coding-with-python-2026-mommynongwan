#!/usr/bin/env python3
print("Enter a number")
try:
    n = int(input())

    for i in range(10):
        result = i * n
        print(f"{i} x {n} = {result}")

except ValueError:
    pass
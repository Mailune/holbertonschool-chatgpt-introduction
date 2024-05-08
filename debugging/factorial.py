#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement n in each iteration
    return result

if len(sys.argv) > 1:
    input_number = int(sys.argv[1])
    f = factorial(input_number)
    print(f)
    
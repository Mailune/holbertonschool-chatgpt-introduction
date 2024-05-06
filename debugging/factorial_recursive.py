#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Parameters:
        n (int): A non-negative integer for which factorial is to be calculated.

    Returns:
        int: The factorial of the input integer n.
    """
    if n == 0:
        # Base case: If n is 0, return 1
        return 1
    else:
        # Recursive case: Multiply n by factorial of (n-1)
        return n * factorial(n-1)

# Calculate factorial of the integer provided as a command-line argument
f = factorial(int(sys.argv[1]))
print(f)

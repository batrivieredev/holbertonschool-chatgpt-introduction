#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer using recursion.

    Parameters:
        n (int): The non-negative integer whose factorial is to be computed.

    Returns:
        int: The factorial of the input integer n.
             If n is 0, the function returns 1 (as 0! = 1).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read an integer input from the command-line arguments
f = factorial(int(sys.argv[1]))

# Print the calculated factorial to the console
print(f)

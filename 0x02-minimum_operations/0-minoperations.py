#!/usr/bin/python3
"""
Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

Define a function that takes an integer as input and returns the minimum number of "Copy All" and "Paste" operations required to get that many "H" characters in a text file
"""


def minOperations(n):
    # If n is less than or equal to 1, return 0 since no operations are needed to get 0 or 1 "H" characters
    if n <= 1:
        return 0
    # Initialize a variable to keep track of the number of operations performed
    ops = 0

    # While n is even, divide n by 2 and count the number of operations required to do so
    while n % 2 == 0:
        ops += 1
        n //= 2

    # Iterate over odd numbers starting from 3 up to the square root of n
    for i in range(3, int(n**0.5)+1, 2):
        # While n is divisible by i, divide n by i and count the number of operations required to do so
        while n % i == 0:
            ops += i
            n //= i

    # If n is greater than 2, add n to the total number of operations required
    if n > 2:
        ops += n

    # Return the total number of operations required to get n "H" characters in the text file
    return ops

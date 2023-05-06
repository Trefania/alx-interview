#!/usr/bin/python3
"""
Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

Define a function that takes an integer as input and returns the minimum number of "Copy All" and "Paste" operations required to get that many "H" characters in a text file
"""

# This function takes an integer n as input and returns the minimum number of operations needed
def minOperations(n):
    if n <= 1:
        return 0  # If n is 0 or 1, it is impossible to get n H's
    i = 2  # Start with the smallest prime number
    result = 0  # Initialize the result to 0
    while i * i <= n:  # Loop until i^2 is greater than n
        while n % i == 0:  # Divide n by i as many times as possible
            result += i  # Add i to the result for each division
            n //= i
        i += 1  # Move to the next prime number
    if n > 1:  # If n is greater than 1, it is a prime factor
        result += n  # Add n to the result
    return result

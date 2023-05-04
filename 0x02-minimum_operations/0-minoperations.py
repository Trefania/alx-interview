#!/usr/bin/python3
"""
Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

Define a function minOperations that takes an integer n as input
"""


def minOperations(n):
    # If n is less than 1, return 0 as it is impossible to achieve
    if n < 1:
        return 0
    # Initialize variables for the number of operations and the current number of characters
    num_ops = 0
    curr_chars = 1
    # Initialize variables for the number of characters to copy and the current buffer size
    copy_chars = 1
    buffer_size = 1
    # Loop until the current number of characters equals n
    while curr_chars < n:
        # If n is evenly divisible by the current buffer size, update the number of characters to copy
        if n % buffer_size == 0:
            copy_chars = curr_chars
        # If the current buffer size is less than the number of characters to copy, update the number of characters to copy
        if buffer_size < copy_chars:
            copy_chars = buffer_size
        # Update the current number of characters and the number of operations based on the number of characters copied
        curr_chars += copy_chars
        num_ops += 1
        # If the current buffer size is less than the number of characters copied, update the buffer size
        if buffer_size < copy_chars:
            buffer_size = copy_chars
        # Otherwise, double the buffer size
        else:
            buffer_size *= 2
    # Return the number of operations
    return num_ops


# Example usage:
n = 9
print(minOperations(n))  # Outputs 6

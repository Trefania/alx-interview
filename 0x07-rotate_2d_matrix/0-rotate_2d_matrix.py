#!/usr/bin/python3
"""Rotates a 2D matrix"""

def rotate_2d_matrix(matrix):
    """the matrix will be rotated 90 degrees clockwise."""
    n = len(matrix)  # Get the size of the matrix (number of rows/columns)

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            # Swap elements across the diagonal
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]  # Reverse the row elements in-place

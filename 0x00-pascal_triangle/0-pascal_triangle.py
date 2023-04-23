#!/usr/bin/python3
"""A script to determine pascal's triangle for any number"""


def pascal_triangle(x):
    """
    returns a representation of the Pascal’s triangle of n
    """
    triangle = [] 
    if x <= 0:  
        return triangle
    for i in range(a): 
        temp_list = [] 
        for a in range(i+1):
            if a == 0 or a == i:
                temp_list.append(1)
            else:
                temp_list.append(triangle[i-1][a-1] + triangle[i-1][a])
        triangle.append(temp_list)  # append temp list to return list
    return triangle

#!/usr/bin/python3
"""A script to determine pascal's triangle for any number"""


def pascal_triangle(x):
    """
    returns a representation of the Pascal’s triangle of n
    """

    triangle = []  # init empty list to be printed
    if x <= 0:  # print empty list if x==0
        return triangle
    for i in range(x):  #0 to x
        temp_list = []  # initialize temporary list for each iterate
        # inner loop
        for a in range(i+1):
            if a == 0 or a == i:
                # add 1 at beginning and end of lists
                temp_list.append(1)
            else:  # add 2 opposite values to get new value
                temp_list.append(triangle[i-1][a-1] + triangle[i-1][a])
        triangle.append(temp_list)  # add temp list to return list
        #print triangle
    return triangle

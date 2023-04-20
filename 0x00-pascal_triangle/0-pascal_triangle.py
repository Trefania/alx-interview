# This Script solves the pascal principle

def factorial(number):
    if (number == 1) or (number == 0):
        return 1
    return (number * factorial(number-1)) # multiplication

def pascal_triangle(n): # n = number
    triangle = [] # empty list
    if (n <= 0): # conditional statement for number less than 1
        return triangle
    for x in range(0, n): # iterate through 0 to (number-1) x is row number
        temp = [] # temporary empty list
        for y in range(0, x+1): # iterate through 0 to (x+1) y is column number
            print(x,y)
            temp.append(Combination(x, y)) # called the combination function
            
        
        triangle.append(temp)
    
    return (triangle)


def Combination(x, y):
    # print("I am base fact",factorial(y) * factorial(x-y))
    return int(factorial(x)/(factorial(y)*factorial(x-y)))

#   0 1 2 3
# 0# 1
# 1# 1 1
# 2# 1 2 1
# 3# 1 3 3 1

# Combination = nCr n!/r!*(n-r)!
# n = no of current row
# r = no of current column
# 0C0 = 2!/1!*(2-1)! = 2/1

# Factorial = n(n-1)!
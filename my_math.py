# Andrew Kirk
# QCC Student ID: 24885486
# Qingyun Li
# QCC Student ID: 24467146
# Queensborough Community College
# ET574 Python Programming - Section M
# Project 2: Math Function Library
# my_math.py
# Shared library for Andrew Kirk and Qingyun Li.

"""
function name: factorial
purpose: Returns the factorial of n (n! = 1 x 2 x ... x n). 0! is 1.
Returns None if n is not an integer or is negative.
parameters: n (int): a whole number that is 0 or greater.
return value(s): (int): the factorial of n, or None if n is invalid.
"""

def factorial(n):
    # Step 1: n must be an integer
    if type(n) != int:
        return None

    # Step 2: n cannot be negative
    if n < 0:
        return None

    # Step 3: multiply 1 x 2 x ... x n
    result = 1
    for i in range(1, n + 1):
        result *= i

    # Step 4: return the answer
    return result


"""
function name: sqrt
purpose: Calculates the square root of a non-negative number.
author: Andrew Kirk
parameters: x (int or float): A non-negative number.
return value(s): (float): The square root of x.
"""

def sqrt(x):
    # Step 1: Check if x is a number (int or float)
    if not isinstance(x, (int, float)):
        raise TypeError("sqrt(x) requires a number")
    # Step 2: Check if x is non-negative
    if x < 0:
        raise ValueError("x must be non-negative")
    # Step 3: Calculate the square root using exponentiation
    return x ** 0.5


"""
function name: area_of_circle
purpose: Calculates the area of a circle with a non-negative radius.
author: Andrew Kirk
parameters: radius (int or float): A non-negative radius.
return value(s): (float): The area in square units.
"""

def area_of_circle(radius):
    # Step 1: Check if radius is a number (int or float).
    if not isinstance(radius, (int, float)):
        raise TypeError("area_of_circle(radius) requires a number")

    # Step 2: Check if radius is non-negative.
    if radius < 0:
        raise ValueError("radius must be non-negative")

    # Step 3: Calculate the area using pi times the radius squared.
    PI = 3.141592653589793
    return PI * radius ** 2

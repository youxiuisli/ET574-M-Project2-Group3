# my_math.py
# Qingyun Li - QCC ID: (24467146)
# Andrew Kirk - QCC ID: 

"""
function name: factorial
purpose: Computes the factorial of a non-negative integer n
(n! = 1 x 2 x 3 x ... x n) using an iterative approach.
By definition, 0! = 1. The function also validates the input
to ensure it is a non-negative integer.
parameters: n (int): A non-negative integer whose factorial will be computed.
return value(s): (int): The factorial of n.
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


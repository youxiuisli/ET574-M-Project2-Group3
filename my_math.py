# my_math.py
# Qingyun Li - QCC ID: (24467146)
# Andrew Kirk - QCC ID: 

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


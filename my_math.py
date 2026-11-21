# my_math.py

"""

Please provide the description of the function.
function name: fibonacci 
purpose: Computes the nth number in the Fibonacci sequence using an iterative approach. 
The function also validates the input to ensure it is a non-negative integer.
parameters: n (int): A non-negative integer representing 
the position in the Fibonacci sequence.
return value(s): (int): The nth Fibonacci number.

"""

def fibonacci(n):

    if not isinstance(n, int):
        raise TypeError("fibonacci(n) requires an integer n")
    if n < 0:
        raise ValueError("n must be non-negative")

    if n < 2:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b



"""

Please provide the description of the function.
function name: mean
purpose: Calculates the average (arithmetic mean) of a collection of numeric values. 
The function validates that all elements are numbers and ensures the input is not empty.
parameters: A collection (e.g., list, tuple) of numeric values (integers or floats).
return value(s): (float): The average of the input values
"""

def mean(values):

    total = 0.0
    count = 0

    for v in values:
        if not isinstance(v, (int, float)):
            raise TypeError("mean() expects all elements to be numbers")
        total += float(v)
        count += 1

    if count == 0:
        raise ValueError("mean() of empty data")

    return total / count

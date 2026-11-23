# ET574 Project 2: Math Function Library

Andrew Kirk
QCC Student ID: 24885486
Qingyun Li
QCC Student ID: 24467146
Queensborough Community College
ET574 Python Programming - Section M
Fall 2026

## Project Overview

G3 A-TEAM will build a shared library containing four mathematical functions.
Each member will implement one approved core function and one original function.
Implementations will use material covered in the course and will not import Python's math module.

Repository: https://github.com/youxiuisli/ET574-M-Project2-Group3

## Project Status

Qingyun implemented and documented factorial(n).
Andrew implemented sqrt(x) and area_of_circle(radius), with four test methods for each,
and added four cross-test methods for factorial(n). All twelve test methods pass locally.
Andrew's implementations and tests are included on main; Qingyun's peer review is pending.
is_prime(n) and its tests remain to be implemented.
The tracker records the instructor collaborator task as complete.

## Files

- my_math.py: all four group functions and their descriptions.
- test_math.py: unit tests for the group's functions.
- README.md: project description, responsibilities, testing assignments, and instructions.
- issuetracker.csv: tasks and issues, owners, dates, status, and related commit references.

Andrew and Qingyun will each add their assigned functions to my_math.py and
their own tests and cross-tests to test_math.py. Both members will maintain the
README and tracker, review each other's pull requests, and verify the combined library.
The ownership table records planned responsibilities; completed contributions
and PR references will be documented as work is merged.

## Members and Function Ownership

| Member      | GitHub Username | Core Function | Original Function      |
| ----------- | --------------- | ------------- | ---------------------- |
| Andrew Kirk | andrewtapin     | sqrt(x)       | area_of_circle(radius) |
| Qingyun Li  | youxiuisli      | factorial(n)  | is_prime(n)            |

Andrew's functions will calculate the square root of a non-negative number and
the area of a circle with a non-negative radius. Qingyun's functions will calculate
the factorial of a non-negative integer and determine whether an integer is prime.
Each function description will specify its accepted inputs, purpose, parameters,
return value, and invalid-input behavior before cross-testing begins.

## Testing Assignments

| Member      | Own Functions to Test           | Partner's Functions to Cross-Test |
| ----------- | ------------------------------- | --------------------------------- |
| Andrew Kirk | sqrt(x), area_of_circle(radius) | factorial(n), is_prime(n)         |
| Qingyun Li  | factorial(n), is_prime(n)       | sqrt(x), area_of_circle(radius)   |

Each member will write at least three cases for each function assigned for testing,
covering typical inputs, edge cases, and invalid inputs. Both members will also test
their own functions. Tests will follow the supplied unittest examples.
Both members will review the complete library and run the combined test suite.

## Requirements

Python 3 is required. The library and tests will use Python's standard library;
no third-party packages are needed.

## Using the Library

This project is an importable function library. Run Python from the repository root.
The currently implemented functions can be used as follows:

```python
from my_math import sqrt, factorial, area_of_circle

print(sqrt(25))
print(factorial(5))
print(area_of_circle(2))
```

Expected results are 5.0, 120, and approximately 12.566370614359172, respectively.
sqrt(x) accepts non-negative integers and floats. It raises TypeError for nonnumeric
input and ValueError for negative input. factorial(n) accepts non-negative integers
and returns None for invalid input, as specified by Qingyun's function description.
area_of_circle(radius) accepts non-negative integers and floats and returns the area
in square units. It raises TypeError for nonnumeric input and ValueError for negative input.
is_prime(n) will be added in a later step.

## Running the Tests

Run the current tests from the repository root:

```text
python -m unittest -v test_math.py
```

The current suite contains twelve test methods: four for sqrt, four for area_of_circle,
and four cross-tests for factorial. The original sample tests for fibonacci and mean have been replaced.
Additional tests will be added when is_prime is implemented and partner testing is completed.

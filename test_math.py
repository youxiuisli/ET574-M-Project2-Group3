# Andrew Kirk
# QCC Student ID: 24885486
# Qingyun Li
# QCC Student ID: 24467146
# Queensborough Community College
# ET574 Python Programming - Section M
# Project 2: Math Function Library
# test_math.py
# Unit tests for the Math Function Library.

import unittest
from my_math import sqrt, factorial


class TestMyMath(unittest.TestCase):
    # Andrew Kirk: tests for sqrt().

    # Check square roots of an integer and a float.
    def test_sqrt_basic(self):
        self.assertAlmostEqual(sqrt(25), 5.0)
        self.assertAlmostEqual(sqrt(2.25), 1.5)

    # Check zero and one.
    def test_sqrt_edge_cases(self):
        self.assertAlmostEqual(sqrt(0), 0.0)
        self.assertAlmostEqual(sqrt(1), 1.0)

    # A negative number must raise ValueError.
    def test_sqrt_negative(self):
        with self.assertRaises(ValueError):
            sqrt(-1)

    # A string must raise TypeError, even if it contains digits.
    def test_sqrt_invalid_type(self):
        with self.assertRaises(TypeError):
            sqrt("25")


    # Andrew Kirk: cross-tests for Qingyun Li's factorial().

    # Check factorials of positive integers.
    def test_factorial_basic(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)

    # Zero factorial and one factorial are both one.
    def test_factorial_edge_cases(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)

    # The function description specifies None for negative input.
    def test_factorial_negative(self):
        self.assertEqual(factorial(-1), None)

    # Floats and strings are invalid, according to the description.
    def test_factorial_invalid_type(self):
        self.assertEqual(factorial(3.5), None)
        self.assertEqual(factorial("5"), None)


if __name__ == "__main__":
    unittest.main(verbosity=2)

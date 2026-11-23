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
from my_math import sqrt, factorial, area_of_circle


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


    # Andrew Kirk: tests for area_of_circle().

    # Check an integer radius and a decimal radius.
    def test_area_of_circle_basic(self):
        self.assertAlmostEqual(area_of_circle(2), 12.566370614359172)
        self.assertAlmostEqual(area_of_circle(2.5), 19.634954084936208)

    # Check a zero radius and a radius smaller than one.
    def test_area_of_circle_edge_cases(self):
        self.assertAlmostEqual(area_of_circle(0), 0.0)
        self.assertAlmostEqual(area_of_circle(0.5), 0.7853981633974483)

    # A negative radius must raise ValueError.
    def test_area_of_circle_negative(self):
        with self.assertRaises(ValueError):
            area_of_circle(-1)

    # A string must raise TypeError, even if it contains digits.
    def test_area_of_circle_invalid_type(self):
        with self.assertRaises(TypeError):
            area_of_circle("2")


if __name__ == "__main__":
    unittest.main(verbosity=2)

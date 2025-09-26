"""This module defines the TestTriangle class.

Usage: 
    To execute all tests in the terminal execute the following command:

    $ python -m unittest tests/test_triangle.py
"""

__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"

import unittest
from shape.triangle import Triangle

def main():
    """ Attribute set to input value."""
    try:
        Triangle("red", 5, 6, 7)
    except ValueError as e:
        print(e)

    """Exception raised when color is blank."""
    try:
        Triangle(" ", 5, 6, 7)
    except ValueError as e:
        print(e)

    """Exception raised when side_1 is not an integer(string)."""
    try:
        Triangle("red", "five", 6, 7)
    except ValueError as e:
        print(e)

    """Exception raised when side_1 is not an integer(float)."""
    try:
        Triangle("red", 5.5, 6, 7)
    except ValueError as e:
        print(e)

    """Exception raised when side_2 is not an integer(string)."""
    try:
        Triangle("red", 5, "six", 7)
    except ValueError as e:
        print(e)

    """Exception raised when side_2 is not an integer(float)."""
    try:
        Triangle("red", 5, 6.5, 7)
    except ValueError as e:
        print(e)

    """Exception raised when side_3 is not an integer(string)."""
    try:
        Triangle("red", 5, 6, "seven")
    except ValueError as e:
        print(e)

    """Exception raised when side_3 is not an integer(float)."""
    try:
        Triangle("red", 5, 6, 7.5)
    except ValueError as e:
        print(e)

    """Exception raised when sides do not satisfy Triangle Inequality Theorem."""
    try:
        Triangle("red", 1, 2, 3)
    except ValueError as e:
        print(e)

    """Returns string format appropriately."""
    try:
        print(Triangle("red", 5, 6, 7))
    except ValueError as e:
        print(e)

    """Returns correct value for calculated_area."""
    try:
        print(Triangle("red", 3, 4, 5).calculate_area())
    except ValueError as e:
        print(e)

    """Returns correct value for calculate_perimeter."""
    try:
        print(Triangle("red", 3, 4, 5).calculate_parameter())
    except ValueError as e:
        print(e)

main
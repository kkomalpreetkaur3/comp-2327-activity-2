"""This module defines the TestRectangle class.

Usage: 
    To execute all tests in the terminal execute the following command:

    $ python tests/test_rectangle.py
"""

__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from shape.rectangle import Rectangle

def main():
    """Attribute set to input values."""
    try:
        Rectangle("red", 5, 6)
    except ValueError as e:
        print(e)

    """Exception raised when color is blank."""
    try:
        Rectangle(" ", 5, 6)
    except ValueError as e:
        print(e)

    """Exception raised when length is not an integer(string)."""
    try:
        Rectangle("red", "five", 6)
    except ValueError as e:
        print(e)

    """Exception raised when length is not an integer(float)."""
    try:
        Rectangle("red", 5.5, 6)
    except ValueError as e:
        print(e)

    """Exception raised when width is not an integer(string)."""
    try:
        Rectangle("red", 5, "six")
    except ValueError as e:
        print(e)

    """Exception raised when width is not an integer(float)."""
    try:
        Rectangle("red", 5, 6.5)
    except ValueError as e:
        print(e)

    """Returns string format appropriately."""
    try:
        print(Rectangle("red", 5, 6))
    except ValueError as e:
        print(e)

    """Returns correct value for calculate_area."""
    try:
        print(Rectangle("red", 3, 4).calculate_area())
    except ValueError as e:
        print(e)

    """Returns correct value for calculate_perimeter."""
    try:
        print(Rectangle("red", 3, 4).calculate_perimeter())
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
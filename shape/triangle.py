"""This module defines the Triangle class."""

__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"

from shape.shape import Shape

class Triangle(Shape):
    """
    Class representing a triangle, inheriting from shape.
    """

    def __init__(self, color: str, side_1: int, side_2: int, side_3: int):
        """
        Initialises a Triangle object based on received arguments (if valid).

        Args:
           color (str): The color of the triangle.
           side_1 (int): Length of the first side.
           side_2 (int): Length of the second side.
           side_3 (int): Length of the third side.

        Raises:
           ValueError: If sides are not numeric or do not satisfy Triangle inequality theorem.
        """
        super().__init__(color)
        if isinstance(side_1, int):
            self._side_1 = side_1
        else:
            raise ValueError("Side 1 must be numeric.")
        if isinstance(side_2, int):
            self._side_2 = side_2
        else:
            raise ValueError("Side 2 must be numeric.")
        if isinstance(side_3, int):
            self._side_3 = side_3
        else:
            raise ValueError("Side 3 must be numeric.")
        if not (self._side_1 + self._side_2 > self._side_3 and
                self._side_1 + self._side_3 > self._side_2 and
                self._side_2 + self._side_3 > self._side_1):
            raise ValueError("The sides do not satisfy the Triangle Inequality Theorem.")
        
    def __str__(self) -> str:
        """
        Returns a string representation of the Triangle.

        Returns:
            str: Description of the triangle including color and sides.
        """
        return (super().__str__() + "\nThis triangle has three sides with the lengths of " +
                f"{self._side_1}, {self._side_2} and {self._side_3} centimeters.")
    
    def calculate_area(self):
        """
        Calculates the area of the triangle using Heron's formula.

        Returns:
           floats: The area of the triangle.
        """
        sp = (self._side_1 + self._side_2 + self._side_3) / 2
        area = (sp * (sp - self._side_1) * (self._side_2) * (self._side_3)) ** 0.5
        return area
    
    def calculate_perimeter(self):
        """
        Calculates the perimeter of the triangle.

        Returns:
            int: The perimeter of the triangle.
        """ 
        return self._side_1 + self._side_2 + self._side_3
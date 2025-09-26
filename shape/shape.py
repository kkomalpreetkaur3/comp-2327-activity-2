"""This module defines the Shape class."""

__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class Shape(ABC):
    """
    Abstract base class representing a shape with a color.
    """

    def __init__(self, color: str):
        """
        Initializes a Shape object based upon received arguments (if valid).

        Args:
            color (str): The color of the shape.

        Raises:
            ValueError: If color is blank.
        """
        if len(color.strip()) == 0:
            raise ValueError("Color cannot be blank.")
        self._color = color

    def __str__(self) -> str:
        """
        Returns a string representation of the Shape.

        Returns:
            str: Description of the shape's color.
        """
        return f"The shape color is {self._color}."
    
    @abstractmethod
    def calculate_area(self):
        """
        Abstract method to calculate the area of the shape.

        Returns:
            float: The area of the shape.
        """
        pass

        @abstractmethod
        def calculate_perimeter(self):
            """
            Abstract method to calculate the perimeter of the shape.

            Returns:
               float: The perimeter of the shape.
            """
            pass
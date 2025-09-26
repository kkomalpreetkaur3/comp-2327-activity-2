"""This module defines the Rectangle class."""

__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"

from .shape import Shape

class Rectangle(Shape):
    """
    Class representing a rectangle, inheriting from shape.
    """

    def __init__(self, color: str, length: int, width: int):
        """
        Initializes a Rectangle object based upon received arguments (if valid).

        Args:
            color (str): The color of the rectangle.
            length (int): Length of the rectangle.
            width (int): Width of the rectangle.

        Raises:
            ValueError: If length or width is not numeric
        """
        super().__init__(color)
        if isinstance(length, int):
            self._length = length
        else:
            raise ValueError("Length must be numeric.")
        if isinstance(width, int):
            self._width = width
        else:
            raise ValueError("Width must be numeric.")
        
        def __str__(self) -> str:
            """
            Returns a string representation of the Rectangle.

            Returns:
                str: Description of the rectangle including color and sides.
            """
            return (super().__str__() + "\nThis rectangle has four sides with the lengths of " +
                f"{self._length}, {self._width}, {self._length} and {self._width} centimeters.")
    
        def calculate_area(self):
            """
            Calculates the area of the rectangle.

            Returns:
                int: The area of the rectangle.
            """
            return self._length * self._width
    
        def calculate_perimeter(self):
            """
            Calculates the perimeter of the rectangle.
            
            Returns:
                int: The perimeter of the rectangle.
            """
            return 2 * (self._length + self._width)


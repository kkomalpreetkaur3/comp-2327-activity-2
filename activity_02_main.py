""""A client program written to verify correctness of the activity 
classes.
"""

__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"
__credits__ = ""

from shape import *

def main():
    """Test the functionality of the methods encapsulated 
    in this project.
    """

    # In the statements coded below, ensure that any statement that 
    # could result in an exception is handled.  When exceptions are 
    # 'caught', display the exception message to the console.

    # *** PART 1 ***
    print("*************PART 1****************")

    # 1. Create an empty list of Shape objects.
    shapes = []


    # 2. Code a statement which creates an instance of the Triangle 
    # class.
    # Append the Triangle to the list of shapes.
    try:
        triangle1 = Triangle("red", 3, 4, 5)
        shapes.append(triangle1)
    except ValueError as e:
        print(e)


    # 3. Code a statement which creates an instance of the Rectangle 
    # class.
    # Append the Rectangle to the list of shapes.
    try:
        rectangle1 = Rectangle("blue", 5, 6)
        shapes.append(rectangle1)
    except ValueError as e:
        print(e)


    # 4. Code 3 additional statements which creates an instance of 
    # Triangle or Rectangle classes (your choice).
    # Append these instances to the list of shapes.
    colors = ["green", "yellow", "purple"]
    sides = [(6, 8, 10), (4, 7), (5, 5, 6)]
    for i in range(3):
        try:
            if len(sides[i]) == 3:
                shape = Triangle(colors[i], *sides[i])
            else:
                shape = Rectangle(colors[i], sides[i][0], sides[i][1])
            shapes.append(shape)
        except ValueError as e:
            print(e)

    # 5. Iterate through the list of shapes.  
    # On each iteration:
    # - print the shape
    # - print the area of the shape to 2 decimal places
    # - print the perimeter of the shape to 2 decimal places
    for shape in shapes:
        try:
            print(shape)
            print(f"Area: {shape.calculate_area():.2f}")
            print(f"Perimeter: {shape.calculate_perimeter():.2f}")
        except ValueError as e:
            print(e)
            
    # *** END PART 1 ***


if __name__ == "__main__":
    main()
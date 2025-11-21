# DZ 15.1. Class Rectangle
class Rectangle:
    """
    A class that describes a rectangle with width and height.
    Supports:
    - area calculation,
    - area comparison,
    - addition of areas of rectangles,
    - multiplication of area by a number,
    - str output of information.
    """

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def get_square(self) -> float:
        """Calculates the area of a rectangle."""
        return self.width * self.height

    def __eq__(self, other) -> bool:
        """
        Compares two rectangles by area.
        Args:
        other (Rectangle): another rectangle
        Returns:
        bool: True if the areas are equal
        """
        return self.get_square() == other.get_square()

    def __add__(self, other):
        """
        Adds two rectangles by area and returns a new rectangle.
        The width of the new rectangle is chosen to be 1,
        height = sum of the areas.
        """
        area = self.get_square() + other.get_square()
        return Rectangle(1, area)

    def __mul__(self, n: float):
        """
        Multiplies the area of a rectangle by n and
        returns a new rectangle.
        Width of the new rectangle = 1, height = area * n.
        """
        new_area = self.get_square() * n
        return Rectangle(1, new_area)

    def __str__(self) -> str:
        return f"Прямокутник: ширина = {self.width}, висота = {self.height}"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
print(r1.get_square())  # == 8, 'Test1'
print(r2.get_square())  # == 18, 'Test2'

r3 = r1 + r2
print(r3.get_square())  # == 26, 'Test3'

r4 = r1 * 4
print(r4.get_square())  # == 32, 'Test4'

print(Rectangle(3, 6) == Rectangle(2, 9))  # == True 'Test5'

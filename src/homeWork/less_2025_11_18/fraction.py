# DZ 15.2. Class "Proper fraction"
class Fraction:
    """
    Class for working with common fractions.
    Supported: addition, subtraction, multiplication, comparison.
    """

    def __init__(self, numerator: int, denominator: int) -> None:
        """
        Creates a new fraction.
        denominator cannot be zero.
        """
        if denominator == 0:
            raise ValueError("Знаменник не може бути нулем.")

        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        """
        Adding fractions.
        Formula:
        a/b + c/d = (a*d + c*b) / (b*d)
        """
        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        """
        Subtracting fractions.
        Formula:
        a/b - c/d = (a*d - c*b) / (b*d)
        """
        new_num = self.numerator * other.denominator - other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        """
        Multiplying fractions.
        Formula:
        (a/b) * (c/d) = (a*c) / (b*d)
        """
        new_num = self.numerator * other.numerator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __eq__(self, other) -> bool:
        """
        Comparing fractions for equality without reduction.
        Comparing by value:
        a/b == c/d if a*d == c*b
        """
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __lt__(self, other) -> bool:
        """
        Less:
        a/b < c/d if a*d < c*b
        """
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __gt__(self, other) -> bool:
        """
        More:
        a/b > c/d if a*d > c*b
        """
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __str__(self) -> str:
        """Returns the format 'Fraction: a, b' """
        return f"Fraction: {self.numerator}, {self.denominator}"


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
print(str(f_c))  # == 'Fraction: 21, 18'
f_d = f_b * f_a
print(str(f_d))  # == 'Fraction: 6, 18'
f_e = f_a - f_b
print(str(f_e))  # == 'Fraction: 3, 18'

print(f_d < f_c)  # True
print(f_d > f_e)  # True
print(f_a != f_b)  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
print(f_1 == f_2)  # True

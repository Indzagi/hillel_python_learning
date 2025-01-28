class Fraction:
    """
    Class allows you to create a correct fractional
    number using arithmetic operations to multiply,
    sum and subtract fractions, as well as compare
    using logical operators
    """

    def __init__(self, a: int, b: int) -> None:
        """
        Function initializes proper fraction where
        'a' is numerator and 'b' is denominator
        :param a: int value numerator
        :param b: int value denominator
        """
        self.a = a
        self.b = b

    def __mul__(self, other: object) -> object:
        """
        Function multiplies two proper fractions and
        initializes the result into a new proper fraction object
        :param other: object
        :return: object
        """
        return Fraction(self.a * other.a, self.b * other.b)

    def __add__(self, other: object) -> object:
        """
        Function sums two proper fractions using the optional
        'arithmetic operations' function, returning the sum
        as a new proper fraction object
        :param other: object
        :return: object
        """
        return self.arithmetic_operations("+", other)

    def __sub__(self, other: object) -> object:
        """
        Function subtracts the second proper fraction from
        the first using the additional 'arithmetic operations'
        function, returning the difference as a new proper fraction object
        :param other: object
        :return: object
        """
        return self.arithmetic_operations("-", other)

    def __eq__(self, other: object) -> bool:
        """
        Function compares two proper fractions and returns a bool value
        :param other: object
        :return: bool
        """
        return self.a / self.b == other

    def __gt__(self, other: object) -> bool:
        """
        Function using the additional function 'logical_operator'
        compares the base value greater than the second one
        :param other: object
        :return: bool
        """
        return self.logical_operator(">", other)

    def __lt__(self, other: object) -> bool:
        """
        Function using the additional function 'logical_operator'
        compares whether the base value is less than the second one
        :param other: object
        :return: bool
        """
        return self.logical_operator("<", other)

    def __ne__(self, other: object) -> bool:
        """
        Function using the additional function 'logical_operator'
        compares whether the base value is not equal to the second
        :param other: object
        :return: bool
        """
        return self.logical_operator("!=", other)

    def arithmetic_operations(self, sign: str, other: object) -> object:
        """
        Helper function receives an arithmetic sign and, depending on the
        sign, performs the arithmetic operation of addition or subtraction,
        returning a new result object
        :param sign: str arithmetic sign
        :param other: object
        :return: new object
        """
        if self.b == other.b:
            if sign == "+":
                return Fraction(self.a + other.a, self.b)
            elif sign == "-":
                return Fraction(self.a - other.a, self.b)
        else:
            denominator = self.b * other.b
            numerator = 0
            if sign == "+":
                numerator = self.a * other.b + other.a * self.b
            elif sign == "-":
                numerator = self.a * other.b - other.a * self.b
            return Fraction(numerator, denominator)

    def logical_operator(self, sign: str, other: object) -> bool:
        """
        Helper function takes a logical operator and returns
        a boolean value depending on the operator
        :param sign: str
        :param other: object
        :return: bool
        """
        if self.b == other.b:
            if sign == ">":
                return self.a > other.a
            elif sign == "<":
                return self.a < other.a
            elif sign == "!=":
                return self.a != other.a
        else:
            if sign == ">":
                return self.a * other.b > other.a * self.b
            elif sign == "<":
                return self.a * other.b < other.a * self.b
            elif sign == "!=":
                return self.a * other.b != other.a * self.b

    def __str__(self):
        """
        Function returns with the values numerator
        and denominator numbers
        :return: str
        """
        return f"Fraction: {self.a}, {self.b}"


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'
assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')

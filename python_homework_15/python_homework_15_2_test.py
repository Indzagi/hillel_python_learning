class Fraction:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def __mul__(self, other: object) -> object:
        return Fraction(self.a * other.a, self.b * other.b)

    def __add__(self, other: object) -> object:
        #        if self.b == other.b:
        #            return Fraction(self.a + other.a, self.b)
        #        else:
        #            denominator = self.b * other.b
        #            numerator = self.a * other.b + other.a * self.b
        #            return Fraction(numerator, denominator)
        return self.arithmetic_operations("+", other)

    def __sub__(self, other: object) -> object:
        #        if self.b == other.b:
        #            return Fraction(self.a - other.a, self.b)
        #        else:
        #            denominator = self.b * other.b
        #            numerator = self.a * other.b - other.a * self.b
        #            return Fraction(numerator, denominator)
        return self.arithmetic_operations("-", other)

    def __eq__(self, other: object) -> object:
        return self.a / self.b == other

    def __gt__(self, other: object) -> object:
        if self.b == other.b:
            return self.a > other.a
        else:
            return self.a * other.b > other.a * self.b

    def __lt__(self, other: object) -> object:
        if self.b == other.b:
            return self.a < other.a
        else:
            return self.a * other.b < other.a * self.b

    def __ne__(self, other: object) -> object:
        if self.b == other.b:
            return self.a != other.a
        else:
            return self.a * other.b != other.a * self.b

    def arithmetic_operations(self, sign: str, other: object) -> object:
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



    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
print(f_c)
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
print(f_d)
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
print(f_e)
assert str(f_e) == 'Fraction: 3, 18'
assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True

print('OK')

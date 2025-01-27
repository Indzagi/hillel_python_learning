class Rectangle:
    """
    The class initializes a rectangle with width and height parameters.
    Using the 'get_square' function, you can get the area, as well as
    compare two areas of different rectangles. Sum the areas of two
    rectangles creating a new object with an area comparable to the
    sum of the areas of the base rectangles.
    Increase the area of the base rectangle by the value 'n',
    creating a new rectangle object whose area is equal to the
    result of the multiplier of the base rectangle with the value 'n'.
    """

    def __init__(self, width: float or int, height: float or int) -> None:
        """
        Function initializes the height and width
        parameters of object - rectangle
        :param width: float or int
        :param height: float or int
        """
        self.width = width
        self.height = height

    def get_square(self) -> float or int:
        """
        Function returns the perimeter of the rectangle
        :return: float or int
        """
        return self.width * self.height

    def __eq__(self, other: object) -> bool:
        """
        Function compares the areas of two rectangles
        and returns a bool value
        :param other: object
        :return: bool
        """
        return self.get_square() == other

    def __add__(self, other: object) -> object:
        """
        Function sums the areas of two rectangles and returns
        a new rectangle object whose area is equal to the
        sum of the two summed
        :param other: object
        :return: new object
        """
        width = self.width if self.width > other.width else other.width
        return Rectangle(width, (self.get_square() +
                                 other.get_square()) / width)

    def __mul__(self, n: float or int) -> object:
        """
        Function returns a new rectangle object
        with sides whose area is equal to a multiplier
        of the base one with value n
        :param n: int
        :return: new object
        """
        return Rectangle(self.width * n, self.height)

    def __str__(self) -> str:
        """
        Function returns the area of the rectangle
        :return: str
        """
        return f"{self.get_square()}"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'
r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'
r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'
r5 = r2 * 4
assert r5.get_square() == 72, 'Test5'
assert Rectangle(3, 6) == Rectangle(2, 9), 'Test6'
print("OK")

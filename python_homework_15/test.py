"""class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Перевантаження оператора додавання
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

# Використання перевантаження оператора
point1 = Point(1, 2)
point2 = Point(3, 4)
result = point1 + point2
print(result.x, result.y)"""  # Вивід: 4 6

a = 4
b = 5
a *= b
print(a)

import math


def calculate_circle_area(radius):
    return round(math.pi * radius ** 2, 2)


assert calculate_circle_area(5) == 78.54, 'Test1'
assert calculate_circle_area(0) == 0, 'Test2'
assert calculate_circle_area(10) == 314.16, 'Test3'
assert calculate_circle_area(2.5) == 19.63, 'Test4'
assert calculate_circle_area(7) == 153.94, 'Test5'
print("ОК")

def perimeter(a, b=0, c=0):
    if b and c:
        return perimetr_triangle(a, b, c)
    else:
        return perimetr_square(a)


def perimetr_triangle(a, b, c):
    return a + b + c


def perimetr_square(a):
    return a * 4

def square(a, b, figure: str):
    if figure == "triangle":
        return triangle_square(a, b)
    if figure == "rectangle":
        return rectangle_square(a, b)


def triangle_square(a, h):
    return a * h / 2


def rectangle_square(a, b):
    return a * b

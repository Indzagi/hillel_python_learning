from math import pi


def volume(a, b, figure, c=0):
    if figure == "parallelepiped":
        return volume_parallelepiped(a, b, c)
    elif figure == "cone":
        return volume_cone(a, b)
    else:
        raise ValueError("Введіть правильну назву фігури")


def volume_parallelepiped(a, b, h):
    return a * b * h


def volume_cone(r, h):
    return 1 / 3 * pi * r ** 2 * h

from inspect import isgenerator


def square(x):
    """
    Функція отримує число та повертає його зведене у квадрат
    :param x: int or float
    :return: значення x зведене у квадрат
    """
    return x ** 2


def some_gen(begin, end, func):
    """
    Функція-генератор, яка отримує перший елемент послідовності,
    кількість елементів послідовнсоті, та функцію для обробки послідовності
    та повертає по одному числу послідовності відносно функції
     begin: перший елемент послідовності
     end: кількість елементів у послідовності
     func: функція, яка формує значення для послідовності
    """
    while end > 0:
        yield begin
        begin = func(begin)
        end -= 1


gen = some_gen(2, 4, square)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')

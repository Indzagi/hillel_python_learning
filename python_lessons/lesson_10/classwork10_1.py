from random import randint
from time import time

"""додаэ до списску н кількість значень до списку
повертає список
повертає список ціле число
100 елементів
створити декоратор (скільки секунд потрібно для цоього функція time)"""


def my_decorate(func):
    def my_dec_func(*args, **kwargs):
        my_first_time = time()
        my_func = func(*args, **kwargs)
        my_second_time = time()
        print(f"My decor fanc: {func.__name__} decorate time {round(my_second_time - my_first_time, 10)} sec")
        return my_func

    return my_dec_func


@my_decorate
def my_list_function(numbers):
    return [randint(1, 100) for i in range(numbers)]


print(my_list_function(99999))

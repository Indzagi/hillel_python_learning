def factorial(num):
    """
    Обчислює факторіал числа num.
    :param num:  Ціле число.
    :return: Факторіал числа num.
    """
    if num == 1:
        return num
    elif num == 0:
        return 1
    elif num < 0:
        return RecursionError
    else:
        return num * factorial(num - 1)


assert factorial(5) == 120
assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(10) == 3628800
assert factorial(-1) == RecursionError
print("OK")

# print(factorial(5))
#print(factorial(0))
#print(factorial(1))
#print(factorial(10))
#print(factorial(-1))
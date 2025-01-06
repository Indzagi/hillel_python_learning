def calculator(num1, num2, operation):
    """
    Реалізує простий калькулятор для двох чисел.

    :param num1: Перше число.
    :param num2: Друге число.
    :param operation: Операція (додавання, віднімання, множення, ділення).
    :return: Результат операції.
    """
    result = 0
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return round(num1 / num2, 2)
    else:
        return result


assert calculator(5, 3, '+') == 8
assert calculator(5, 3, '-') == 2
assert calculator(5, 3, '*') == 15
assert calculator(5, 3, '/') == 1.67
assert calculator(5, 3, 'unknown') == 0
print("OK")


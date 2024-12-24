"""мини калькулятор базові функуции відтворювати
корінь квадратний"""


def sum_function(numb1, numb2):
    return numb1 + numb2


def subtraction_function(numb1, numb2):
    return numb1 - numb2


def multiplication_function(numb1, numb2):
    return numb1 * numb2


def division_function(numb1, numb2):
    return numb1 / numb2


def calculation(numb1, arithmetic, numb2=0):
    if arithmetic == "+":
        print(sum_function(numb1, numb2))
    elif arithmetic == "-":
        print(subtraction_function(numb1, numb2))
    elif arithmetic == "*":
        print(multiplication_function(numb1, numb2))
    elif arithmetic == "/":
        if numb2 == 0:
            print("Не можна ділити на 0")
        else:
            print(division_function(numb1, numb2))


calculation(2, "+", 6)

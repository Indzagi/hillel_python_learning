num1 = int(input('Введіть перше значення: '))
num2 = int(input('Введіть друге значення: '))
mat_sign = input('Введіть тип математичної дії + - * /: ')

if mat_sign == '+':
    summ = num1 + num2
    print('Сумма значень =', summ)

elif mat_sign == '-':
    minus = num1 - num2
    print('Віднімання значень =', minus)

elif mat_sign == '*':
    multi = num1 * num2
    print('Множина значень =', multi)

elif mat_sign == '/':
    text_true = 'Ділення значень ='
    text_false = 'Дільник не може = 0'
    division = print(text_true, round(num1 / num2, 8)) if num2 != 0 else print(text_false)

else:
    print('Введіть коректне значення математичної дії на прикладі: \n + \n - \n * \n /')

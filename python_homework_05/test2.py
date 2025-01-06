print('\nДобрий день, для коректної работи потрібно вводити арифметичний вираз у форматі \'а + b\' \n')
on_off_calc = 'y'
result = 0

while on_off_calc == 'y':
    my_len = input('Введіть, що треба розрахувати: ')
    my_second_len = my_len.split()
    firs_digit, second_digit = int(my_second_len[0]), int(my_second_len[2])
    mat_func = my_second_len[1]
    if len(my_second_len) > 3:
        print(f'Не правильна кількість вводимих значень')
        continue
    elif mat_func == '+':
        result = firs_digit + second_digit
    elif mat_func == '-':
        result = firs_digit - second_digit
    elif mat_func == '*':
        result = firs_digit * second_digit
    elif mat_func == '/':
        if second_digit != 0:
            result = round(firs_digit / second_digit, 8)
        else:
            print('Не можна ділити на 0')
            continue
    print(f'\n{my_len} = {result}\n')
    on_off_calc = input('Для продовження введіть y: ')
    if on_off_calc != 'y':
        break

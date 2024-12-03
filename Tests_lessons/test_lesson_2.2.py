number5 = int(input('Будь ласка, введіть 5-ти значне число: '))

first_numb, second_numb = divmod(number5 // 1000, 10)
third_numb, fourth_numb = divmod(number5 // 10 % 100, 10)
fifth_numb = number5 % 10

print(f'{fifth_numb}{fourth_numb}{third_numb}{second_numb}{first_numb}')

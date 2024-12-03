number5 = int(input('Будь ласка, введіть 5-х значне число: '))

first_numb = number5 // 10000
second_numb = number5 % 10000 // 1000
third_numb = number5 % 1000 // 100
fourth_numb = number5 % 100 // 10
fifth_numb = number5 % 10

revers_numb = f'{fifth_numb}{fourth_numb}{third_numb}{second_numb}{first_numb}'
print(revers_numb)
number4 = int(input('Будь ласка, введіть 4-х значне число: '))

first_numb = number4 // 1000
print(first_numb)

second_numb = number4 // 100 % 10
print(second_numb)

third_numb = number4 // 10 % 100 % 10
print(third_numb)

print(number4 % 10)



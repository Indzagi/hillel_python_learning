number4 = int(input('Будь ласка, введіть 4-х значне число: '))

numb_int1, numb_rem1 = divmod(number4 // 100, 10)
numb_int2, numb_rem2 = divmod(number4 % 100, 10)

print(f'{numb_int1} \n{numb_rem1}\n{numb_int2}\n{numb_rem2}')
def sum_of_digits(number):
    my_text_numb = str(number).replace("-", "")
    return sum([int(numb) for numb in my_text_numb])


assert sum_of_digits(123) == 6, 'Test1'
assert sum_of_digits(-456) == 15, 'Test2'
assert sum_of_digits(789) == 24, 'Test3'
assert sum_of_digits(0) == 0, 'Test4'
assert sum_of_digits(-9876) == 30, 'Test5'
print("ОК")

from keyword import iskeyword
from string import punctuation

my_string = input('Введіть ім\'я змінної для перевірки: ')
my_string_len = len(my_string)
my_int = 0

if (my_string[0].isdigit()
        or ' ' in my_string
        or iskeyword(my_string)
        or my_string.count('_', 0, 2) > 1):
    print(False)
else:
    while my_string_len:
        txt_temp = my_string[my_int]
        my_string_len -= 1
        my_int += 1
        if txt_temp == '_':
            continue
        if txt_temp.istitle() or txt_temp in punctuation:
            print(False)
            break
    else:
        print(True)

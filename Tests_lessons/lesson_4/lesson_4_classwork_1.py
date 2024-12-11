my_list = []
count = 10

while count:
    my_list.append(int(input('Введіть значення: ')))
    print(my_list)
    count -= 1
print(sum(my_list))

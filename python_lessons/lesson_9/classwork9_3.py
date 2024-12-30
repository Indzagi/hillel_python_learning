my_list = [1, -2, 3, -10, 0]
# print(list(filter(lambda digit: digit >= 0, my_list)))
print(list(map(lambda lst: sum(my_list), my_list))[0])

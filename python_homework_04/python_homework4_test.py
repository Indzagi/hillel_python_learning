my_list = [0, 9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0, 1]
# my_list = [1, 0, 13, 0, 0, 0, 5]
# my_list = [0]
# my_list = [0, 1, 0, 12, 3]
count_nulls = my_list.count(0)

while count_nulls:
    temp_null = my_list.pop(my_list.index(0))
    my_list.append(temp_null)
    count_nulls -= 1
else:
    print(my_list)

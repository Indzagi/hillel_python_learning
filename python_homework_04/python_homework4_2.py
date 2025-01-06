my_list = [0, 1, 7, 2, 4, 8]
# my_list = [1, 3, 5]
# my_list = [6]
# my_list = []

if len(my_list) > 1:
    my_list_len = round(len(my_list) / 2)
    my_temp_list = []
    temp_index = 0

    while my_list_len:
        my_temp_list.append(my_list[temp_index])
        temp_index += 2
        my_list_len -= 1
    else:
        print(sum(my_temp_list) * my_list[-1])

elif len(my_list) == 1:
    print(my_list[0] ** 2)
else:
    print(0)

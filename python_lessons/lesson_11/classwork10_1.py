def numb_sort(my_list):
    my_len = len(my_list)
    for first in range(my_len - 1):
        for second in range(0, my_len - first - 1):
            if my_list[second] > my_list[second + 1]:
                temp_list = my_list[second]
                my_list[second] = my_list[second + 1]
                my_list[second + 1] = temp_list


my_numb = [95, 24, 35, 1, 23, 15, 99, 6, 55, 41]
print(my_numb)
numb_sort(my_numb)
print(my_numb)

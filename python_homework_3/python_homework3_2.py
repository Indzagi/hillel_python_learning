my_list = [1, 2, 3, 4, 5]
my_list2 = [0]

if not my_list:
    print(my_list)
else:
    my_list2[0] = my_list.pop()
    my_list_final = my_list2 + my_list
    print(my_list_final)

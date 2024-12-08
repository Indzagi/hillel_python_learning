my_base_list = [1, 2, 3, 4, 5, 6, 7]

if len(my_base_list) % 2 == 0:
    first_lend = int(len(my_base_list) / 2)
    second_lend = len(my_base_list) - first_lend

else:
    first_lend = int(len(my_base_list) / 2 + 1)
    second_lend = len(my_base_list) - first_lend

my_first_list = my_base_list [0:first_lend]
my_second_list = my_base_list [first_lend:len(my_base_list)]

my_list_final = [my_first_list, my_second_list]
print(my_list_final)
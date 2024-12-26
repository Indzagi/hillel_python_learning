import random

my_list = [random.randint(1, 10) for i in range(random.randrange(3, 11))]
my_new_list = [my_list[0], my_list[2], my_list[-2]]
print(my_list, my_new_list, sep=' => ')

import random


def common_elements():
    my_set_1 = {random.randrange(0, 100, 3) for i in range(100)}
    my_set_2 = {random.randrange(0, 100, 5) for i in range(100)}
    my_set_split = my_set_1.intersection(my_set_2)
    print(my_set_split)
    return my_set_split


assert common_elements()

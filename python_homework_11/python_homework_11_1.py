def prime_generator(end = 0):
    value = 2
    my_list = list()
    my_list.append(value)
    if value % value - 1  == 0:

    print(my_list)
    return my_list


from inspect import isgenerator

"""gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')"""

prime_generator ()
#print(list(prime_generator(10)))
#print(list(prime_generator(15)))
#print(list(prime_generator(29)))

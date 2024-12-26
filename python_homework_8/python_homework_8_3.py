def find_unique_value(some_list):
    my_set = set()
    #   for i in some_list:
    #      my_firs_set.add(i)
    #   print(my_firs_set)
    return [num for num in some_list if num not in my_set and not my_set.add(num)]


print(find_unique_value([1, 2, 1, 1]))
print(find_unique_value([2, 3, 3, 3, 5, 5]))
print(find_unique_value([5, 5, 5, 2, 2, 0.5]))
# assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
# assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
# assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")

def add_one(some_list):
    return [int(i) for i in str(int("".join(str(numb) for numb in some_list)) + 1)]


assert add_one([1, 2, 3, 4])
assert add_one([9, 9, 9])
assert add_one([0])
assert add_one([9])
print("ОК")

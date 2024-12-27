"""зі списку кортеджей до словника """

data = {
    1: "b",
    2: "x",
    3: "t",
    4: "d",
    5: "a"
}
print(data)
my_list = list(data.items())
print(my_list)
my_list.sort(key=lambda i: i[1])
print(my_list)
my_second_list = dict(my_list)
print(my_second_list)

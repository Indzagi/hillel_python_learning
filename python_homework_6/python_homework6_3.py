my_numb = input("Please, enter a numeric value: ")
my_multiple1 = 10

while my_multiple1 > 9:
    my_numb_list = [int(numb) for numb in my_numb]
    my_multiple1 = 1
    for numb in my_numb_list:
        my_multiple1 *= numb
    if my_multiple1 > 9:
        my_numb = str(my_multiple1)
print(my_multiple1)

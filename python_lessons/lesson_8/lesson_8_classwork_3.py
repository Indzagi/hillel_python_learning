"""дано список з клавіатури 10 значень
залишити тільки унікальні
функція отримую список
залишає тільки унікальні"""


def unic_numbers(mylist):
    my_split_list = mylist.split()
    my_set = set()
    return [int(num) for num in my_split_list if num not in my_set and not my_set.add(num)]


numbers = input("Введіть 10 значень через пробіл: ")
print(unic_numbers(numbers))

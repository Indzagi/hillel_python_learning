def quick_sort(list_of_numbs):
    start, end = 0, len(list_of_numbs) - 1
    while start == (len(list_of_numbs) - 1) / 2:
        if list_of_numbs[start] <= list_of_numbs[end]:
            print()
    pass


my_numb = [95, 24, 35, 1, 23, 15, 99, 6, 55, 41]
print(my_numb)
quick_sort(my_numb)
print(my_numb)

# сортування вибором і вставками

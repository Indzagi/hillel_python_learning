i = 3
r = 'крансий'
g = 'зелений'
b = 'синій'
color = r
cort_color = []

while i:
    give_color = int(input('Введіть ' + color + ' колір в діапазоні від 0 до 255: '))
    print(i)

    if i == 3 and 0 <= give_color <= 255:
        color = g
        i -= 1
        cort_color.append(give_color)
    elif i == 2 and 0 <= give_color <= 255:
        color = b
        i -= 1
        cort_color.append(give_color)

    elif i == 1 and 0 <= give_color <= 255:
        color = b
        i -= 1
        cort_color.append(give_color)
    else:
        print ("Введіть коректне значення")

else:
    cort_color_finish = tuple(cort_color)
    print(cort_color)
    print(cort_color_finish)


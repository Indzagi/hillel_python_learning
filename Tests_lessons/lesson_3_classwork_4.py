#1 площа кола 2 периметр трикутника 3 обсяг паралелепіпеда
import math

numb = int(input('Введіть 1, щоб порахувати площу кола. \n'
                 'Введіть 2, щоб порахувати периметр трикутника. \n'
                 'Введіть 3, щоб порахувати обьєм паралелепіпеда. \n\n'
                 'Введіть значення:'))
if numb == 1:
    r_circle = int(input('\nВведіть радіус круга: '))
    print('Площа кола = ', round(math.pi * r_circle ** 2))

elif numb == 2:
    triangle_a = int(input('\nВведіть сторону трикутику a: '))
    triangle_b = int(input('Введіть сторону трикутику b: '))
    triangle_c = int(input('Введіть сторону трикутику c: '))
    print('Периметр трикутника = ', triangle_b + triangle_b + triangle_c)

elif numb == 3:
    parallelepiped_a = int(input('\nВведіть довжину паралелепіпеду a: '))
    parallelepiped_b = int(input('Введіть ширину паралелепіпеду b: '))
    parallelepiped_h = int(input('Введіть висоту паралелепіпеду h: '))
    print('Обьєм паралелепіпеда = ', parallelepiped_a * parallelepiped_b * parallelepiped_h)

else:
    print('Ви ввели не вірне значення')
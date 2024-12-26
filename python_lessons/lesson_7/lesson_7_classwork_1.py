from collections import namedtuple

"""именований кортеж оцінки
5 людей с 4 предметами

математика
информатика
физика
физ-ра

ручками и мейка
замінити оцінки
за реплейс"""

student = namedtuple('Student', 'name mathematics informatics physics chemistry')

student1 = student('Марія', 10, 11, 9, 8)
student2 = student('Данило', 5, 6, 3, 4)
student3 = student('Марія', 3, 4, 12, 2)
student4 = student('Данило', 4, 6, 5, 1)

print(student1)
student1 = student1._replace(mathematics=12, informatics=11, physics=11, chemistry=12)
print(student1)

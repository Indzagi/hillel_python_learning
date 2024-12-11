""" мала <18,5, нормальна 18,5-25, зайва 25-30, ожирыння >30"""

mass = int(input("Введіть масу тіла (кг): "))
height = float(input("Введіть свій зріст (м): "))

index_mass = mass / (height ** 2)

if index_mass < 18.5:
    print(index_mass, "- Ваша вага мала")
elif 18.5 <= index_mass < 25:
    print(index_mass, "- Ваша вага нормальна")
elif 25 <= index_mass < 30:
    print(index_mass, "- Ваша вага зайва")
elif index_mass >= 30:
    print(index_mass, "- Вітаємо, в вас ожиріння")
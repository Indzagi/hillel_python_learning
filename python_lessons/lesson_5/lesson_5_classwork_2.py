text_put = input('Введіть текст')
text_len = len(text_put)
disk = 0


if text_len <= 10:
    disk = 10
elif 10 < text_len <= 25:
    disk = 20
elif 25 < text_len <= 50:
    disk = 25
else:
    print(f"Ваша скидка {disk}")
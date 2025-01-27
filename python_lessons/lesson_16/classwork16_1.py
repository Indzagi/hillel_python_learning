count = 10
my_text = ""
while count:
    my_text += input(f"Введіть значення: ") + "\n"
    count -= 1

with open("test.txt", 'w', encoding='utf-8') as my_file:
    my_file.write(my_text)

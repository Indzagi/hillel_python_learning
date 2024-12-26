"""1 =послідовність ввесті і подивитись
2 = Имя до послідовності байтів
"""

my_text = input("Input your text here: ")

text_enc = my_text.encode("utf-8")

print(type(text_enc))
print(text_enc)

my_text = text_enc.decode("utf-8")

print(type(my_text))
print(my_text)

print(text_enc.decode("windows-1251"))

"""словник 
бібліотека \
у кожного автора свої рядки \
створити дік 3 - 5 творів""
numb = int(input('Enter a digital: '))
numb = round(numb ** 0.5, 2) if numb >= 0 else numb ** 4
print(numb)
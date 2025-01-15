while True:
    try:
        a = int(input("Enter a: "))
        break
    except ValueError:
        print("Except, input value a to integer")
while True:
    try:
        b = int(input("Enter b: "))
        break
    except ValueError:
        print("Except, input value b to integer")

print(a * b)

def say_hi(name: str, age: int):
    my_txt = f"\nHi. My name is {name} and I'm {age} years old"
    print(my_txt)
    return my_txt


assert say_hi("Alis", 23)
assert say_hi("Petr", 53)

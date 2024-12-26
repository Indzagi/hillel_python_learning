hi_input = input("Enter your name and age: ").split()
name_inp, age_inp = str(hi_input[0]), int(hi_input[1])


def say_hi(name: str, age: int):
    my_txt = f"\nHi. My name is {name} and I'm {age} years old"
    print(my_txt)
    return my_txt


say_hi_enter = say_hi(name_inp, age_inp)

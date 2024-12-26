from string import ascii_letters

my_letters_input = input('Enter a range of letters in the format a-b: ')
first_letter, second_letter = (ascii_letters.index(my_letters_input[0]),
                               ascii_letters.index(my_letters_input[2]))
print(my_letters_input[0]) if first_letter == second_letter else print(ascii_letters[first_letter:second_letter + 1])

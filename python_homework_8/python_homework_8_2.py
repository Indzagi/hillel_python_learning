from string import punctuation


def is_palindrome(text):
    text = text.lower().replace(' ', '')
    text = ''.join(i for i in text if i not in punctuation)
    my_text_len = int(len(text) / 2)
    my_index = 0
    my_index_end = -1
    while my_index != my_text_len:
        if text[my_index] == text[my_index_end]:
            my_index += 1
            my_index_end -= 1
        else:
            return False
    return True


assert is_palindrome('A man, a plan, a canal: Panama') == True
assert is_palindrome('0P') == False
assert is_palindrome('a.') == True
assert is_palindrome('aurora') == False
print("ОК")

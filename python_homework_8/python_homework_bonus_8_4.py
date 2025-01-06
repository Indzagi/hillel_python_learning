def reverse_words(sentence):
    my_list = sentence.split()
    my_list_len = len(my_list)
    my_string = ""
    i = 0
    while i < my_list_len:
        my_string += f"{"".join(reversed(my_list[i]))}{" " if i < my_list_len - 1 else ""}"
        i += 1
    return my_string


assert reverse_words("Hello world") == "olleH dlrow", 'Test1'
assert reverse_words("Python is fun") == "nohtyP si nuf", 'Test2'
assert reverse_words("Quick brown fox") == "kciuQ nworb xof", 'Test3'
assert reverse_words("Just a test") == "tsuJ a tset", 'Test4'
assert reverse_words("123 456") == "321 654", 'Test5'
print("ОК")

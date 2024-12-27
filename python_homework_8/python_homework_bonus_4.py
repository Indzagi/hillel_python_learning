def reverse_words(sentence):
    my_list = sentence.split()
    my_index = -1
    my_index2 = len(my_list[0])
    print(my_list)
    while my_index2:
        my_string = list(("".join(i for i in my_list[0][my_index])))
        print("врем строка= ", my_string)
#        my_string = list("".join(i for i in my_list[0][my_index]))
        my_index -= 1
        my_index2 -= 1
        print(type(my_string), my_string)
    print("Послід", my_string)
    return my_string


reverse_words("Hello world")
reverse_words("Python is fun")
reverse_words("Quick brown fox")
reverse_words("Just a test")
reverse_words("123 456")
# assert reverse_words("Hello world") == "olleH dlrow", 'Test1'
# assert reverse_words("Python is fun") == "nohtyP si nuf", 'Test2'
# assert reverse_words("Quick brown fox") == "kciuQ nworb xof", 'Test3'
# assert reverse_words("Just a test") == "tsuJ a tset", 'Test4'
# assert reverse_words("123 456") == "321 654", 'Test5'
# print("ОК")

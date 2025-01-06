from string import punctuation

my_len = input('Введіть фразу для хештегу: ')
my_len = my_len.title().replace(' ', '')
my_len = ''.join(i for i in my_len if i not in punctuation)
my_hashtag = '#' + my_len
if len(my_hashtag) > 140:
    my_hashtag = my_hashtag[:140]
print(my_hashtag)

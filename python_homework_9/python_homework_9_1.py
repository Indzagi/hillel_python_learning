def popular_words(text, words):
    """
    Function take text and list of world and return dictionary
    where key is search words and value is words count
    :param text: str
    :param words: list of words
    :return: dictionary
    """
    text_split = text.lower().split()
    my_dict = {key: () for key in words}
    i = 0
    while i < len(my_dict):
        my_dict[words[i]] = text_split.count(words[i])
        i += 1
    return my_dict


assert (popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                      ['i', 'was', 'three', 'near'])) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')

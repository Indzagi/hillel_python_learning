def correct_sentence(text: str):
    text_exp = text.split()
    word1 = text_exp[0].title()
    if len(text_exp) > 1:
        word2 = text_exp[1]
        if word1[-1:] == ".":
            word2 = word2.title()
        text = f"{word1} {word2}"
    else:
        text = f"{word1}"
    text += "." if text[-1:] != "." else ""
    print(text)
    return text


assert correct_sentence("greetings, friends")
assert correct_sentence("hello")
assert correct_sentence("Greetings. Friends")
assert correct_sentence("Greetings, friends.")
assert correct_sentence("greetings, friends.")

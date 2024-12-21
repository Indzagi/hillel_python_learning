def second_index(text: str, some_str: str):
    if text.count(some_str) > 1:
        my_index = text.find(some_str)
        my_index = text.find(some_str, my_index + 1)
        print(my_index)
    else:
        print(None)
        return None
    return my_index


second_index("sims", "s")
second_index("find the river", "e")
second_index("hi", "h")
second_index("Hello, hello", "lo")
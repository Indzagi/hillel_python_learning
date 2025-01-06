def second_index(text: str, some_str: str):
    if text.count(some_str) > 1:
        my_index = text.index(some_str, text.index(some_str) + 1)
        print(my_index)
        return my_index
    else:
        print(None)
        return None


assert second_index("sims", "s")
assert second_index("find the river", "e")
assert second_index("hi", "h") is None
assert second_index("Hello, hello", "lo")

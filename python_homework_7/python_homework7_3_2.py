def second_index(text: str, some_str: str):
    return text.index(some_str, text.index(some_str) + 1) if text.count(some_str) > 1 else None


assert second_index("sims", "s")
assert second_index("find the river", "e")
assert second_index("hi", "h") is None
assert second_index("Hello, hello", "lo")
print('ОК')

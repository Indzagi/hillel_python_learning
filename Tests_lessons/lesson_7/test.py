def second_index(text, symbol):
    if text.find(symbol) != -1:
        if text.find(symbol,text.find(symbol)+1) != -1:
          l=text.find(symbol,text.find(symbol)+1)
          print(l)
        else:
            print(None)
            return None
    else:
        print(None)
        return None
    return l


assert second_index("sims", "s")
assert second_index("find the river", "e")
assert second_index("hi", "h") is None
assert second_index("hi mayorh", "h")
assert second_index("hi mr Mayor", " ")

def capitalize(s):
    even_index = "".join(c.upper() if i % 2 == 0 else c for i, c in enumerate(s))
    odd_index = "".join(c.upper() if i % 2 != 0 else c for i, c in enumerate (s))
    return [even_index, odd_index]
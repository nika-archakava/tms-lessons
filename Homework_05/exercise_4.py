def get_longest_word(text: str):
    s = max(text.split(), key=len)
    return s


m = get_longest_word('Hello nice to meet you')
print(f"The longest word in this text is {m}")

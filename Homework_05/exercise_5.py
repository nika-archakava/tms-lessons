def get_most_frequent_word(text: str):
    list_words = text.split()
    a = {}
    for i in list_words:
        if i not in a:
            a[i] = 1
        else:
            a[i] += 1
    m = 0
    d = ''
    for key, value in a.items():
        if value > m:
            m = value
            d = key
    return d


print(get_most_frequent_word('Hello Hello nice nice nice to meet meet you'))

list_a = list(input().split())


def remove_vowels(lister):
    vowels = ['a', 'i', 'e', 'o', 'u', 'y']
    return list(filter(lambda x: x not in vowels, lister))


print(remove_vowels(list_a))

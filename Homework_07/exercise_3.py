list_a = list(input().split())


def remove_vowels(lister):
    return list(filter(lambda x: x not in ['a', 'i', 'e', 'o', 'u', 'y', 'A', 'I', 'E', 'O', 'U', 'Y'], lister))


print(remove_vowels(list_a))

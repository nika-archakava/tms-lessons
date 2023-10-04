list_a = list(input().split())


def map_to_tuples(y: list):
    return list(map(lambda x: (x.upper(), x.lower()), y))


print(map_to_tuples(list_a))

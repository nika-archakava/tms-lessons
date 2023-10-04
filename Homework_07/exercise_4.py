from functools import reduce

texty = list(input().split())
symbol = input()


def my_join(a, b):
    return reduce(lambda x, y: x + b + y, a)


print(my_join(texty, symbol))

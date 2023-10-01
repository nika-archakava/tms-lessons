def generate_squares(*args: int):
    a = [i ** 2 for i in args]
    return a


print(generate_squares(3, 4, 6, 7, 1, 3))
print(generate_squares(476, 567, 2333))

assert (generate_squares(1, 2, 3)) == [1, 4, 9]

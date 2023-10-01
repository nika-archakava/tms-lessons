def generate_natural_cubes(n: int):
    a = [i ** 3 for i in range(1, n + 1)]
    return a


print(generate_natural_cubes(6))
print(generate_natural_cubes(95))

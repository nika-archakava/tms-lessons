def my_decorator(func):
    def wrapper(x):
        print(f"Function get the result: {x}")
        z = func(x)
        print(f"The result of function: {z}")
        return z

    return wrapper


@my_decorator
def my_func(x):
    return x ** 2


y = my_func(3)
print(f'y={y}')

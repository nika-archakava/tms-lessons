def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function get the result: {args},{kwargs}")
        z = func(*args, **kwargs)
        print(f"The result of function: {z}")
        return z

    return wrapper


@my_decorator
def my_func(a, b, c, d):
    return a + b + c + d


y = my_func(1, 2, c=3, d=4)
print(f'y={y}')

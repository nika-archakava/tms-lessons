def is_year_leap(n: int):
    if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
        return True
    else:
        return False


print(is_year_leap(1999))
print(is_year_leap(2000))
print(is_year_leap(1900))

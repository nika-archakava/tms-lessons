from datetime import date


class Person:
    def __init__(self, full_name: str, age: int, gender: str):
        self.full_name = full_name
        self.age = age
        self.gender = gender

    def print_person_info(self):
        print(f'Person: {self.full_name} ({self.gender}), {self.age} years old')

    def get_birth_year(self):
        return 2023 - self.age

    def new_get_birth_day(self):
        today = date.today()
        return today.year - self.age

# girl = Person('Veranika', 31, 'Female')
# girl.print_person_info()
# print(girl.get_birth_year())
# print(girl.new_get_birth_day())

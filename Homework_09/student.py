class Student:
    def __init__(self, full_name: str, average_mark: float):
        self.full_name = full_name
        self.average_mark = average_mark

    def get_scholarship(self):
        if self.average_mark < 6:
            return 60
        elif 8 > self.average_mark >= 6:
            return 80
        else:
            return 100

    def is_excellent(self):
        return self.average_mark >= 9

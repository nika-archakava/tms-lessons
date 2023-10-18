from student import Student

students = [
    Student("Nasty Pepko", 7),
    Student("Timur Archakau", 9.4),
    Student("Ella Dudzik", 3)
]


def cal_sum_scholarship(list_of_students: list):
    m = 0
    for i in list_of_students:
        m += i.get_scholarship()
    return m


print(cal_sum_scholarship(students))


def get_excellent_student_count(list_of_students: list):
    s = 0
    for i in list_of_students:
        if i.is_excellent() is True:
            s += 1
    return s


print(get_excellent_student_count(students))

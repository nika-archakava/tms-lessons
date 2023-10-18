from person import Person

my_friends = [
    Person("Nasty", 30, "F"),
    Person("Timur", 25, "M"),
    Person("Ella", 29, "F")
]

for i in my_friends:
    i.print_person_info()


def get_oldest_person(list_of_friends: list):
    m = 0
    k = ''
    for friend in list_of_friends:
        if friend.age > m:
            m = friend.age
            k = friend
    return k


get_oldest_person(my_friends).print_person_info()


def filter_male_person(list_of_friends: list):
    male_friends = list(filter(lambda friend: friend.gender == 'M', list_of_friends))
    # male_friends=[friend for friend in my_friends if friend.gender == 'M']
    return male_friends


men = filter_male_person(my_friends)
for i in men:
    i.print_person_info()

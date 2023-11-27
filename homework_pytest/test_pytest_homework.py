import random

import pytest



@pytest.fixture
def print_before_test():
    n = random.randint
    print(f'Random age is {n}')


@pytest.fixture
def fixture_teardown():
    yield
    print("Deleting random age ... Done")


class TestHomework:

    @pytest.mark.wizard
    @pytest.mark.parametrize("first_name", ["John", "Harry", "Ron"])
    @pytest.mark.parametrize("last_name", ["Smith", "Potter", "Weasley"])
    def test_fail_if_john_smith(self, age, print_before_test, first_name, last_name, fixture_teardown):
        if first_name == "John" and last_name == "Smith":
            pytest.xfail("I don't like John Smith!")
        print(f'Hello, {first_name} {last_name}. Your age is {age}')

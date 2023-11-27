import random

import pytest


@pytest.fixture
def age():
    yield random.randrange(0, 100)

import pytest


@pytest.fixture
def valid_username():
    return "rmf40"


@pytest.fixture
def invalid_username1():
    return "invalid username"


@pytest.fixture
def invalid_username2():
    return "Rio%$##@"

import pytest


@pytest.fixture
def valid_name() -> str:
    return "Jad"


@pytest.fixture
def invalid_name1() -> str:
    return "123"


@pytest.fixture
def invalid_name2() -> str:
    return ""


@pytest.fixture
def invalid_name3() -> str:
    return "jad"

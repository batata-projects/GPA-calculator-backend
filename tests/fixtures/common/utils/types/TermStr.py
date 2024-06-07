import pytest


@pytest.fixture
def valid_term():
    return "Fall 2021 - 2022"


@pytest.fixture
def invalid_term():
    return "invalid-term"

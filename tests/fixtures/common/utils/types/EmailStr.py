import pytest


@pytest.fixture
def valid_email():
    return "rmf04@mail.aub.edu"


@pytest.fixture
def invalid_email():
    return "invalid-email"


@pytest.fixture
def invalid_domain():
    return "rmf40@gmail.com"

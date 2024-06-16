import pytest
from pydantic import EmailStr


@pytest.fixture
def valid_email() -> EmailStr:
    return "valid@mail.aub.edu"


@pytest.fixture
def invalid_email() -> EmailStr:
    return "invalid@invalid_domain.com"

import pytest

from src.common.utils.types import PasswordStr


@pytest.fixture
def valid_password() -> PasswordStr:
    return "Password123"


@pytest.fixture
def invalid_password() -> PasswordStr:
    return "invalid-password"

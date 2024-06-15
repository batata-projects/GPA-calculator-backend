import pytest

from src.common.utils.types import UsernameStr


@pytest.fixture
def valid_username() -> UsernameStr:
    return "rmf40"


@pytest.fixture
def invalid_username1() -> UsernameStr:
    return "invalid username"


@pytest.fixture
def invalid_username2() -> UsernameStr:
    return "Rio%$##@"

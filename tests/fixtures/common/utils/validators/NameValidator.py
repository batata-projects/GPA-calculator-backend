import pytest


@pytest.fixture
def valid_name() -> str:
    return "Jad"


@pytest.fixture
def invalid_name() -> None:
    return 123

import pytest

from src.common.utils.types import TermInt


@pytest.fixture
def valid_term() -> TermInt:
    return 202310


@pytest.fixture
def invalid_term() -> TermInt:
    return 2023

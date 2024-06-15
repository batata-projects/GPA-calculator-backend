import pytest

from src.common.utils.types import TermStr


@pytest.fixture
def valid_term() -> TermStr:
    return "Fall 2021 - 2022"


@pytest.fixture
def invalid_term() -> TermStr:
    return "invalid-term"

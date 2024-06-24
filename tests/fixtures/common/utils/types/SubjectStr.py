import pytest

from src.common.utils.types import SubjectStr


@pytest.fixture
def valid_subject() -> SubjectStr:
    return "SUBJECT"


@pytest.fixture
def invalid_subject() -> SubjectStr:
    return None  # type: ignore

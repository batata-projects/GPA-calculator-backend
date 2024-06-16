import pytest

from src.common.session import Session


@pytest.fixture
def session() -> Session:
    return Session(
        access_token="access_token",
        refresh_token="refresh_token",
        expires_in=3600,
    )

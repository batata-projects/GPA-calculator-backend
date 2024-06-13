import pytest

from src.common.responses import Session


@pytest.fixture
def session() -> Session:
    return Session(
        access_token="access_token",
        refresh_token="refresh_token",
        expires_in=3600,
    )

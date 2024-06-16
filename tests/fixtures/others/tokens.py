import pytest


@pytest.fixture
def valid_access_token(valid_jwt: str) -> str:
    return valid_jwt


@pytest.fixture
def invalid_access_token() -> None:
    return None


@pytest.fixture
def valid_refresh_token() -> str:
    return "iL5m3C43Qg_1FVq3mGCNdQ"


@pytest.fixture
def invalid_refresh_token() -> None:
    return None

import pytest


@pytest.fixture
def valid_uuid():
    return "6f6c6d2b-4e4b-4c4f-8c8e-6c6d4e4b3a3b"


@pytest.fixture
def invalid_uuid():
    return "invalid-uuid"

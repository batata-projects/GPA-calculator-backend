from typing import Any

import pytest

from src.auth.schemas import LoginRequest, RegisterRequest


@pytest.fixture
def register_request() -> Any:
    return RegisterRequest(
        first_name="Rayan",
        last_name="Fakhreddine",
        email="new@mail.com",
        password="pasSword123",
    )


@pytest.fixture
def login_request() -> Any:
    return LoginRequest(email="rayan@mail.com", password="pasSword123")

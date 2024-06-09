# create fixtures for auth schemas
#
# Path: tests/fixtures/auth/schemas.py
#
from typing import Any

import pytest
from pydantic import BaseModel, EmailStr

from src.auth.schemas import LoginRequest, RegisterRequest
from src.common.utils.types.PasswordStr import PasswordStr
from src.common.utils.types.UsernameStr import UsernameStr

@pytest.fixture
def register_request() -> Any:
    return(
        RegisterRequest(
            first_name = "Rayan",
            last_name="Fakhreddine",
            email="verynew@aub.edu.lb",
            username="rmf40",
            password="pasSword123",
        )
    )


@pytest.fixture
def login_request() -> Any:
    return( 
        LoginRequest(
            email="rmf40@aub.edu.lb",
            password="pasSword123"
        )
    )

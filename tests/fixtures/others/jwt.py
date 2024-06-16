import time

import jwt
import pytest


@pytest.fixture
def valid_signature() -> str:
    return "SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"


@pytest.fixture
def valid_jwt(valid_signature: str) -> str:
    return jwt.encode(
        {
            "aud": "authenticated",
            "exp": int(time.time()) + 3600,
            "iat": int(time.time()),
        },
        valid_signature,
        algorithm="HS256",
    )


@pytest.fixture
def invalid_jwt(valid_signature: str) -> str:
    return jwt.encode(
        {
            "aud": "authenticated",
            "exp": int(time.time()) - 3400,
            "iat": int(time.time()) - 3600,
        },
        valid_signature,
        algorithm="HS256",
    )

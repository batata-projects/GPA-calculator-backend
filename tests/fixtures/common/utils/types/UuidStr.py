from unittest.mock import Mock

import pytest

from src.common.utils.types import UuidStr


@pytest.fixture
def valid_uuid(uuid4: Mock) -> UuidStr:
    return str(uuid4())


@pytest.fixture
def invalid_uuid() -> UuidStr:
    return "invalid-uuid"

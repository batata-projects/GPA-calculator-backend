import random
import uuid

import pytest

from src.common.utils.types import UuidStr


@pytest.fixture
def valid_uuid() -> UuidStr:
    return str(uuid.UUID(int=random.getrandbits(128)))


@pytest.fixture
def invalid_uuid() -> UuidStr:
    return "invalid-uuid"

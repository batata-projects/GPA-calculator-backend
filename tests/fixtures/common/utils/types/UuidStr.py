import random
import uuid
from unittest.mock import Mock

import pytest

from src.common.utils.types import UuidStr


@pytest.fixture
def uuid_generator() -> Mock:
    return Mock(side_effect=lambda: str(uuid.UUID(int=random.getrandbits(128))))


@pytest.fixture
def invalid_uuid() -> UuidStr:
    return "invalid-uuid"

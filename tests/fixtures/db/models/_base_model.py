from typing import Optional
from unittest.mock import Mock

import pytest

from src.common.utils.types import UuidStr
from src.db.models import BaseModel


class TestObject(BaseModel):
    id: Optional[UuidStr] = None
    name: str


@pytest.fixture
def test_objects(uuid4: Mock) -> list[TestObject]:
    return [
        TestObject(id=str(uuid4()), name="test_name_1"),
        TestObject(id=str(uuid4()), name="test_name_2"),
    ]


@pytest.fixture
def test_object1(test_objects: list[TestObject]) -> TestObject:
    return test_objects[0]


@pytest.fixture
def test_object2(test_objects: list[TestObject]) -> TestObject:
    return test_objects[1]
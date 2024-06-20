from typing import Optional
from unittest.mock import Mock

import pytest

from src.common.utils.types import UuidStr
from src.db.models import BaseModel


class TestObject(BaseModel):
    __test__ = False
    id: Optional[UuidStr] = None
    name: str


@pytest.fixture
def test_objects(uuid4: Mock, valid_uuid: UuidStr) -> list[TestObject]:
    return [
        TestObject(id=valid_uuid, name="test_name_1"),
        TestObject(id=valid_uuid, name="test_name_2"),
    ]


@pytest.fixture
def test_object1(test_objects: list[TestObject]) -> TestObject:
    return test_objects[0]


@pytest.fixture
def test_object2(test_objects: list[TestObject]) -> TestObject:
    return test_objects[1]

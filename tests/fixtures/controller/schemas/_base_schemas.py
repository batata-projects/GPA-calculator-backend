from typing import Optional

import pytest

from src.controller.schemas._base_schemas import BaseQuery
from tests.fixtures.db.models._base_model import TestObject


class TestQuery(BaseQuery[TestObject]):
    name: Optional[str] = None


@pytest.fixture
def test_query() -> TestQuery:
    return TestQuery(name="test_name")

from typing import Any, Optional, get_type_hints

import pytest
from fastapi import Query
from pydantic import BaseModel as PydanticBaseModel
from pydantic import create_model

from tests.fixtures.db.models._base_model import TestObject


@pytest.fixture
def test_query() -> PydanticBaseModel:
    fields = dict(get_type_hints(TestObject))
    queries: dict[str, Any] = {
        key: (Optional[fields[key]], Query(None)) for key in fields if key != "id"
    }
    DynamicModel: type[PydanticBaseModel] = create_model("DynamicModel", **queries)
    return DynamicModel()

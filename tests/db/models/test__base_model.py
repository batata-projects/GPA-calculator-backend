from typing import Any

import pytest

from src.common.utils.data import ValidData
from tests.fixtures.db.models._base_model import TestObject


class TestBaseModel:
    def test_base_model(self, test_object1: TestObject) -> None:
        assert test_object1.id is not None
        assert test_object1.name == "test_name_1"

    @pytest.mark.parametrize(
        "data",
        [
            {"id": ValidData().TestObject.id, "name": "test_name"},
            {"id": ValidData().TestObject.id},
            {"name": "test_name"},
            {},
        ],
    )
    def test_model_validate_partial_parametrized(self, data: dict[str, Any]) -> None:
        TestObject.model_validate_partial(data)

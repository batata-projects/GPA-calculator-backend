from pydantic import BaseModel as PydanticBaseModel

from src.common.utils.types import UuidStr
from src.controller.schemas._base_schemas import BaseQuery, BaseResponse
from tests.fixtures.db.models._base_model import TestObject


class TestBaseQuery:

    def test_base_query(self) -> None:
        assert issubclass(BaseQuery, PydanticBaseModel)


class TestBaseResponse:

    def test_base_response(self, valid_uuid: UuidStr) -> None:
        obj = TestObject(id=valid_uuid, name="test_name")
        response = BaseResponse[TestObject](items=[obj])

        assert response.items == [obj]

    def test_base_response_no_items(self) -> None:
        response = BaseResponse[TestObject]()

        assert response.items == []

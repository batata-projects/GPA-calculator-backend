from typing import Optional

from pydantic import BaseModel as PydanticBaseModel

from src.controller.schemas._base_schemas import BaseQuery, BaseResponse
from src.db.models import BaseModel


class TestObject(BaseModel):
    id: Optional[str] = None
    name: str


class TestBaseQuery:

    def test_base_query(self) -> None:
        assert issubclass(BaseQuery, PydanticBaseModel)


class TestBaseResponse:

    def test_base_response(self) -> None:
        obj = TestObject(id="test_id", name="test_name")
        response = BaseResponse[TestObject](items=[obj])

        assert response.items == [obj]

    def test_base_response_no_items(self) -> None:
        response = BaseResponse[TestObject]()

        assert response.items == []

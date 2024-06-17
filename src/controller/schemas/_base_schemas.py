from typing import Generic, TypeVar

from pydantic import BaseModel as PydanticBaseModel

from src.db.models import BaseModel

BaseModelType = TypeVar("BaseModelType", bound=BaseModel)


class BaseQuery(PydanticBaseModel, Generic[BaseModelType]): ...


class BaseResponse(PydanticBaseModel, Generic[BaseModelType]):
    items: list[BaseModelType] = []

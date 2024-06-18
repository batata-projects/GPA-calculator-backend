from typing import Generic, Optional, TypeVar

from pydantic import BaseModel as PydanticBaseModel

T = TypeVar("T")


class APIResponse(PydanticBaseModel, Generic[T]):
    status: int
    message: str
    data: Optional[T] = None

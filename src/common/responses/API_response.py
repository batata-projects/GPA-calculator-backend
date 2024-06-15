from typing import Generic, Optional, TypeVar

from gotrue.types import Session as GoTrueSession  # type: ignore
from pydantic import BaseModel as PydanticBaseModel

T = TypeVar("T")


class APIResponse(PydanticBaseModel, Generic[T]):
    status: int
    message: str
    data: Optional[T] = None

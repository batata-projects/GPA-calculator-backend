from typing import Generic, Optional, TypeVar

from pydantic import BaseModel as PydanticBaseModel
from src.db.models.users import User
T = TypeVar("T")


class Session(PydanticBaseModel):
    access_token: str
    refresh_token: str
    expires_in: int


class APIResponse(PydanticBaseModel, Generic[T]):
    status: int
    message: str
    data: Optional[T] = None


class AuthResponse(PydanticBaseModel):
    user: Optional[User] = None
    session: Optional[Session] = None

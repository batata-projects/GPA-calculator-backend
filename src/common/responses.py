from typing import Generic, Optional, TypeVar

from pydantic import BaseModel

from src.db.models.users import User

T = TypeVar("T")


class Session(BaseModel):
    access_token: str
    refresh_token: str
    expires_in: int


class APIResponse(BaseModel, Generic[T]):
    status: int
    message: str
    data: Optional[T] = None


class AuthResponse(BaseModel):
    user: Optional[User] = None
    session: Optional[Session] = None

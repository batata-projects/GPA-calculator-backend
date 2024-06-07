from typing import Generic, Optional, TypeVar

from pydantic import BaseModel as PydanticBaseModel

from gotrue.types import Session as SupabaseSession

from src.db.models.users import User

T = TypeVar("T")


class Session(PydanticBaseModel):
    access_token: str
    refresh_token: str
    expires_in: int

    @classmethod
    def validate_supabase_session(cls, session: SupabaseSession) -> "Session":
        return cls(
            access_token=session.access_token,
            refresh_token=session.refresh_token,
            expires_in=session.expires_in,
        )


class APIResponse(PydanticBaseModel, Generic[T]):
    status: int
    message: str
    data: Optional[T] = None


class AuthResponse(PydanticBaseModel):
    user: Optional[User] = None
    session: Optional[Session] = None

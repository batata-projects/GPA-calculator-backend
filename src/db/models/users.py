from typing import Optional

from gotrue.types import User as SupabaseUser  # type: ignore
from pydantic import BaseModel

from src.db.models.utils import EmailStr, UuidStr


class User(BaseModel):
    id: Optional[UuidStr] = None
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    credits: int
    counted_credits: int
    grade: float

    @classmethod
    def validate_supabase_user(cls, user: SupabaseUser) -> "User":
        return cls(
            id=user.id,
            username=user.user_metadata["username"],
            email=user.email,
            first_name=user.user_metadata["first_name"],
            last_name=user.user_metadata["last_name"],
            credits=user.user_metadata["credits"],
            counted_credits=user.user_metadata["counted_credits"],
            grade=user.user_metadata["grade"],
        )

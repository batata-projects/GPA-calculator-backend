from typing import Optional

from gotrue.types import User as GoTrueUser  # type: ignore
from pydantic import EmailStr

from src.common.utils.types import UuidStr
from src.db.models import BaseModel


class User(BaseModel):
    id: Optional[UuidStr] = None
    email: EmailStr
    first_name: str
    last_name: str

    @classmethod
    def validate_supabase_user(cls, user: GoTrueUser) -> "User":
        return cls(
            id=user.id,
            email=user.email,
            first_name=user.user_metadata["first_name"],
            last_name=user.user_metadata["last_name"],
        )

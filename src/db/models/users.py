from typing import Optional

from gotrue.types import User as SupabaseUser  # type: ignore
from pydantic import EmailStr, NonNegativeFloat, NonNegativeInt, field_validator

from src.db.models.utils import BaseModelCustomized, UsernameStr, UuidStr


class User(BaseModelCustomized):
    id: Optional[UuidStr] = None
    email: EmailStr
    username: UsernameStr
    first_name: str
    last_name: str
    credits: NonNegativeInt
    counted_credits: NonNegativeInt
    grade: NonNegativeFloat

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

    @field_validator("email")
    def validate_email_domain(cls, v: str) -> str:
        try:
            domain = v.split("@")[1]
            if domain not in ["aub.edu.lb", "mail.aub.edu"]:
                raise ValueError
        except ValueError:
            raise ValueError(f"{v} is an invalid email")
        return v

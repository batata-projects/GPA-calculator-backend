from typing import Optional

from gotrue.types import User as SupabaseUser  # type: ignore
from pydantic import (
    BaseModel,
    EmailStr,
    NonNegativeFloat,
    NonNegativeInt,
    field_validator,
)

from src.db.models.utils import UsernameStr, UuidStr


class User(BaseModel):
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
        credits = user.user_metadata.get("credits", 0)
        counted_credits = user.user_metadata.get("counted_credits", 0)
        grade = user.user_metadata.get("grade", 0.0)
        return cls(
            id=user.id,
            username=user.user_metadata["username"],
            email=user.email,
            first_name=user.user_metadata["first_name"],
            last_name=user.user_metadata["last_name"],
            credits=credits,
            counted_credits=counted_credits,
            grade=grade,
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



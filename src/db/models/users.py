from typing import Optional

from gotrue.types import User as GoTrueUser  # type: ignore
from pydantic import EmailStr, NonNegativeFloat, NonNegativeInt, field_validator

from src.common.utils.models import BaseModel
from src.common.utils.types import UsernameStr, UuidStr
from src.common.utils.validators.EmailValidator import validate_email


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
    def validate_supabase_user(cls, user: GoTrueUser) -> "User":
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
    def email_validator(cls, v: str) -> str:
        return validate_email(v)

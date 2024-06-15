from typing import Optional

from gotrue.types import User as GoTrueUser  # type: ignore
from pydantic import BaseModel as PydanticBaseModel
from pydantic import EmailStr, Field, NonNegativeFloat, NonNegativeInt

from src.common.utils.types import UsernameStr
from src.db.models import User


class UserRequest(PydanticBaseModel):
    email: EmailStr = Field(..., description="Email")
    username: UsernameStr = Field(..., description="Username")
    first_name: str = Field(..., description="First name")
    last_name: str = Field(..., description="Last name")
    credits: Optional[NonNegativeInt] = Field(None, description="Credits")
    grade: Optional[NonNegativeFloat] = Field(None, description="Grade")


class UserResponse(PydanticBaseModel):
    users: list[User] = []

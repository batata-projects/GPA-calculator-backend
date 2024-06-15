from gotrue.types import User as GoTrueUser  # type: ignore
from pydantic import BaseModel as PydanticBaseModel
from pydantic import EmailStr, Field, NonNegativeFloat, NonNegativeInt

from src.common.utils.types.UsernameStr import UsernameStr
from src.db.models.users import User


class UserRequest(PydanticBaseModel):
    email: EmailStr = Field(..., description="Email")
    username: UsernameStr = Field(..., description="Username")
    first_name: str = Field(..., description="First name")
    last_name: str = Field(..., description="Last name")
    credits: NonNegativeInt = Field(None, description="Credits")
    grade: NonNegativeFloat = Field(None, description="Grade")


class UserResponse(PydanticBaseModel):
    users: list[User] = []

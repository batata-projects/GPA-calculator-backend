from pydantic import BaseModel as PydanticBaseModel

from src.db.models.users import User


class UserResponse(PydanticBaseModel):
    users: list[User] = []

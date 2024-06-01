from pydantic import BaseModel

from src.db.models.users import User


class UserResponse(BaseModel):
    users: list[User] = []

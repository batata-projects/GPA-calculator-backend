from typing import Optional

from pydantic import EmailStr, NonNegativeFloat, NonNegativeInt

from src.controller.schemas._base_schemas import BaseQuery
from src.db.models import User


class UserQuery(BaseQuery[User]):
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    credits: Optional[NonNegativeInt] = None
    counted_credits: Optional[NonNegativeInt] = None
    grade: Optional[NonNegativeFloat] = None

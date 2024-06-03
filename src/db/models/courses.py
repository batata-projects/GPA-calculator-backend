from typing import Optional

from pydantic import BaseModel, PositiveFloat

from src.db.models.utils import UuidStr


class Course(BaseModel):
    id: Optional[UuidStr] = None
    available_course_id: UuidStr
    user_id: UuidStr
    grade: Optional[PositiveFloat] = None
    passed: Optional[bool] = None

from typing import Optional

from pydantic import BaseModel

from src.db.models.utils import UuidStr


class Course(BaseModel):
    id: Optional[UuidStr] = None
    user_id: UuidStr
    all_courses_id: UuidStr
    grade: Optional[float] = None

from typing import Optional

from pydantic import BaseModel

from src.db.models.utils import CourseCodeStr, CourseNameStr, UuidStr


class AvailableCourse(BaseModel):
    id: Optional[UuidStr] = None
    terms_id: UuidStr
    name: CourseNameStr
    code: CourseCodeStr
    credits: int
    graded: bool

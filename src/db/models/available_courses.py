from typing import Optional

from pydantic import BaseModel

from src.db.models.utils import CourseCodeStr, CourseNameStr, UuidStr


class AvailableCourse(BaseModel):
    id: Optional[UuidStr] = None
    term_id: UuidStr
    name: CourseNameStr
    code: CourseCodeStr
    credits: int
    graded: bool

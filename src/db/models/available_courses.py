from typing import Optional

from pydantic import BaseModel

from src.db.models.utils import CourseCodeStr, CourseNameStr, TermStr, UuidStr


class AvailableCourse(BaseModel):
    id: Optional[UuidStr] = None
    name: CourseNameStr
    code: CourseCodeStr
    credits: int
    term_name: TermStr
    graded: bool

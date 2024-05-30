from typing import Optional

from pydantic import BaseModel

from src.db.models.utils import CourseCodeStr, CourseNameStr, TermStr, UuidStr


class AvailableCourse(BaseModel):
    id: Optional[UuidStr] = None
    course_name: CourseNameStr
    course_code: CourseCodeStr
    credits: int
    terms_name: TermStr
    graded: bool
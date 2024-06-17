from typing import Optional

from pydantic import NonNegativeInt

from src.common.utils.types import CourseCodeStr, CourseNameStr, UuidStr
from src.db.models import BaseModel


class AvailableCourse(BaseModel):
    id: Optional[UuidStr] = None
    term_id: UuidStr
    name: CourseNameStr
    code: CourseCodeStr
    credits: NonNegativeInt
    graded: bool

from typing import Optional

from pydantic import NonNegativeInt

from src.common.utils.models import BaseModel
from src.common.utils.types import CourseCodeStr, CourseNameStr, UuidStr


class AvailableCourse(BaseModel):
    id: Optional[UuidStr] = None
    term_id: UuidStr
    name: CourseNameStr
    code: CourseCodeStr
    credits: NonNegativeInt
    graded: bool

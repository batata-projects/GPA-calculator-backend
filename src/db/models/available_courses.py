from typing import Optional

from pydantic import NonNegativeInt

from src.db.models.utils import (
    BaseModelCustomized,
    CourseCodeStr,
    CourseNameStr,
    UuidStr,
)


class AvailableCourse(BaseModelCustomized):
    id: Optional[UuidStr] = None
    term_id: UuidStr
    name: CourseNameStr
    code: CourseCodeStr
    credits: NonNegativeInt
    graded: bool

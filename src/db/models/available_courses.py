from typing import Optional

from pydantic import NonNegativeInt

from src.common.utils.models.BaseModel import BaseModel
from src.common.utils.types.CourseCodeStr import CourseCodeStr
from src.common.utils.types.CourseNameStr import CourseNameStr
from src.common.utils.types.UuidStr import UuidStr


class AvailableCourse(BaseModel):
    id: Optional[UuidStr] = None
    term_id: UuidStr
    name: CourseNameStr
    code: CourseCodeStr
    credits: NonNegativeInt
    graded: bool

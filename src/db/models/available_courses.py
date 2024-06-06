from typing import Optional

from pydantic import NonNegativeInt

from src.db.models.utils.models.BaseModel import BaseModel
from src.db.models.utils.types.CourseCodeStr import CourseCodeStr
from src.db.models.utils.types.CourseNameStr import CourseNameStr
from src.db.models.utils.types.UuidStr import UuidStr


class AvailableCourse(BaseModel):
    id: Optional[UuidStr] = None
    term_id: UuidStr
    name: CourseNameStr
    code: CourseCodeStr
    credits: NonNegativeInt
    graded: bool

from typing import Optional

from src.common.utils.models import BaseModel
from src.common.utils.types import CourseGradeFloat, UuidStr


class Course(BaseModel):
    id: Optional[UuidStr] = None
    available_course_id: UuidStr
    user_id: UuidStr
    grade: Optional[CourseGradeFloat] = None
    passed: Optional[bool] = None

from typing import Optional

from src.common.utils.types import CourseGradeFloat, UuidStr
from src.db.models import BaseModel


class Course(BaseModel):
    id: Optional[UuidStr] = None
    available_course_id: UuidStr
    user_id: UuidStr
    grade: Optional[CourseGradeFloat] = None
    passed: Optional[bool] = None

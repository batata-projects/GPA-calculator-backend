from typing import Optional

from src.common.utils.types import CourseGradeFloat, UuidStr
from src.controller.schemas._base_schemas import BaseQuery
from src.db.models import Course


class CourseQuery(BaseQuery[Course]):
    available_course_id: Optional[UuidStr] = None
    user_id: Optional[UuidStr] = None
    grade: Optional[CourseGradeFloat] = None
    passed: Optional[bool] = None

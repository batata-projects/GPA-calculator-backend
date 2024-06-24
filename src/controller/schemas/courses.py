from typing import Optional

from src.common.utils.types import CourseCodeStr, CourseGradeFloat, SubjectStr, UuidStr
from src.controller.schemas._base_schemas import BaseQuery
from src.db.models import Course


class CourseQuery(BaseQuery[Course]):
    user_id: Optional[UuidStr] = None
    subject: Optional[SubjectStr] = None
    course_code: Optional[CourseCodeStr] = None
    term: Optional[int] = None
    credits: Optional[int] = None
    grade: Optional[CourseGradeFloat] = None
    graded: Optional[bool] = None

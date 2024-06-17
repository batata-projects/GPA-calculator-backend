from typing import Optional

from pydantic import NonNegativeInt

from src.common.utils.types import CourseCodeStr, CourseNameStr, UuidStr
from src.controller.schemas._base_schemas import BaseQuery
from src.db.models import AvailableCourse


class AvailableCourseQuery(BaseQuery[AvailableCourse]):
    term_id: Optional[UuidStr] = None
    name: Optional[CourseNameStr] = None
    code: Optional[CourseCodeStr] = None
    credits: Optional[NonNegativeInt] = None
    graded: Optional[bool] = None

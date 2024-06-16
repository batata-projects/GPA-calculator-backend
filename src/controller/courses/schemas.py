from typing import Optional

from pydantic import BaseModel as PydanticBaseModel
from pydantic import Field

from src.common.utils.types import CourseGradeFloat, UuidStr
from src.db.models import Course


class CourseRequest(PydanticBaseModel):
    available_course_id: UuidStr = Field(..., description="Available course ID")
    user_id: UuidStr = Field(..., description="User ID")
    grade: Optional[CourseGradeFloat] = Field(None, description="Grade")
    passed: Optional[bool] = Field(None, description="Passed")


class CourseResponse(PydanticBaseModel):
    courses: list[Course] = []

from pydantic import BaseModel as PydanticBaseModel
from pydantic import Field, NonNegativeFloat

from src.common.utils.types.UuidStr import UuidStr
from src.db.models.courses import Course


class CourseRequest(PydanticBaseModel):
    available_course_id: UuidStr = Field(..., description="Available course ID")
    user_id: UuidStr = Field(..., description="User ID")
    grade: NonNegativeFloat = Field(None, description="Grade")
    passed: bool = Field(None, description="Passed")


class CourseResponse(PydanticBaseModel):
    courses: list[Course] = []

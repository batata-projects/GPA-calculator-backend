from pydantic import BaseModel as PydanticBaseModel
from pydantic import Field, NonNegativeInt

from src.common.utils.types.CourseCodeStr import CourseCodeStr
from src.common.utils.types.CourseNameStr import CourseNameStr
from src.common.utils.types.UuidStr import UuidStr
from src.db.models.available_courses import AvailableCourse


class AvailableCourseRequest(PydanticBaseModel):
    term_id: UuidStr = Field(..., description="Term ID")
    name: CourseNameStr = Field(..., description="Course name")
    code: CourseCodeStr = Field(..., description="Course code")
    credits: NonNegativeInt = Field(..., description="Credit")
    graded: bool = Field(..., description="Graded")


class AvailableCourseResponse(PydanticBaseModel):
    available_courses: list[AvailableCourse] = []

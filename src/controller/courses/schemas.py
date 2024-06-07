from pydantic import BaseModel as PydanticBaseModel

from src.db.models.courses import Course


class CourseResponse(PydanticBaseModel):
    courses: list[Course] = []

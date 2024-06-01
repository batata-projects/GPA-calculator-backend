from pydantic import BaseModel

from src.db.models.courses import Course


class CourseResponse(BaseModel):
    courses: list[Course] = []

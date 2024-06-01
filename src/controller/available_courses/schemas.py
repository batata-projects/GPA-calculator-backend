from pydantic import BaseModel

from src.db.models.available_courses import AvailableCourse


class AvailableCourseResponse(BaseModel):
    available_courses: list[AvailableCourse] = []

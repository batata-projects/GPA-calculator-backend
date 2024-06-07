from pydantic import BaseModel as PydanticBaseModel

from src.db.models.available_courses import AvailableCourse


class AvailableCourseResponse(PydanticBaseModel):
    available_courses: list[AvailableCourse] = []

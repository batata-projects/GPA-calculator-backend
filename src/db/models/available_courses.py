from typing import Any, Optional

from pydantic import BaseModel, NonNegativeInt

from src.db.models.utils import (
    CourseCodeStr,
    CourseNameStr,
    UuidStr,
    validate_bool,
    validate_course_code,
    validate_course_name,
    validate_non_negative_int,
    validate_uuid,
)


class AvailableCourse(BaseModel):
    id: Optional[UuidStr] = None
    term_id: UuidStr
    name: CourseNameStr
    code: CourseCodeStr
    credits: NonNegativeInt
    graded: bool

    @classmethod
    def model_validate_partial(cls, data: dict[str, Any]):
        if "id" in data:
            validate_uuid(data["id"])
        if "term_id" in data:
            validate_uuid(data["term_id"])
        if "name" in data:
            validate_course_name(data["name"])
        if "code" in data:
            validate_course_code(data["code"])
        if "credits" in data:
            validate_non_negative_int(data["credits"])
        if "graded" in data:
            validate_bool(data["graded"])
        for key in data:
            if key not in cls.model_fields:
                raise ValueError(f"{key} is not a valid field")

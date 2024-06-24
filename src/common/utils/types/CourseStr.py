from typing import Annotated

from pydantic.functional_validators import BeforeValidator


def validate_course_str(v: str) -> str:
    if not v:
        raise ValueError("Course str cannot be empty")
    if not v.isnumeric() and not v.isupper():
        raise ValueError("Letters in course str must be in uppercase")
    return v


CourseStr = Annotated[str, BeforeValidator(validate_course_str)]

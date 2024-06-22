from typing import Annotated

from pydantic.functional_validators import BeforeValidator


def validate_course_code_str(v: str) -> str:
    if not v:
        raise ValueError("Course code cannot be empty")
    return v.upper()


CourseCodeStr = Annotated[str, BeforeValidator(validate_course_code_str)]

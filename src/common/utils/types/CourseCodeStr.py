from typing import Annotated

from pydantic.functional_validators import BeforeValidator


# TODO: Add tests
def validate_course_code_str(v: str) -> str:
    if not v:
        raise ValueError("Course code cannot be empty")
    if not v.isnumeric() and not v.isupper():
        raise ValueError("Letters in course code must be in uppercase")
    return v


CourseCodeStr = Annotated[str, BeforeValidator(validate_course_code_str)]

from typing import Annotated, Optional

from pydantic.functional_validators import BeforeValidator


def validate_course_name(v: Optional[str] = None) -> Optional[str]:
    if not v:
        return None
    try:
        if len(v) != 4 or not v.isalpha():
            raise ValueError
        return v
    except ValueError:
        raise ValueError(f"{v} is an invalid course name")


CourseNameStr = Annotated[str, BeforeValidator(validate_course_name)]

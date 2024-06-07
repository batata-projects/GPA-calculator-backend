from typing import Annotated, Optional

from pydantic.functional_validators import BeforeValidator


def validate_course_code(v: Optional[str] = None) -> Optional[str]:
    if not v:
        return None
    try:
        if len(v) < 3 or len(v) > 5 or not v.isalnum() or v[0].isalpha():
            raise ValueError
        return v
    except ValueError:
        raise ValueError(f"{v} is an invalid course code")


CourseCodeStr = Annotated[str, BeforeValidator(validate_course_code)]

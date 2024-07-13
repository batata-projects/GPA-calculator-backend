from typing import Annotated

from pydantic.functional_validators import BeforeValidator


def validate_course_grade_float(v: float) -> float:
    if v not in [-1, 0.0, 1, 1.3, 1.7, 2, 2.3, 2.7, 3, 3.3, 3.7, 4, 4.3]:
        raise ValueError(f"{v} is an invalid grade")
    return v


CourseGradeFloat = Annotated[float, BeforeValidator(validate_course_grade_float)]

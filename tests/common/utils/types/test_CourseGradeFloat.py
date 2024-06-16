import pytest

from src.common.utils.types.CourseGradeFloat import (
    CourseGradeFloat,
    validate_course_grade,
)


class TestCourseGradeFloat:
    def test_course_grade_float_successful(
        self, valid_course_grade_float: CourseGradeFloat
    ) -> None:
        assert (
            validate_course_grade(valid_course_grade_float) == valid_course_grade_float
        )

    def test_course_grade_float_invalid(
        self, invalid_course_grade_float: CourseGradeFloat
    ) -> None:
        with pytest.raises(ValueError):
            validate_course_grade(invalid_course_grade_float)

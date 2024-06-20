import pytest

from src.common.utils.types.CourseReferenceNumberStr import (
    CourseReferenceNumberStr,
    validate_course_reference_number_str,
)


class TestCourseReferenceNumberStr:
    def test_course_reference_number_str_successful(
        self, valid_course_reference_number: CourseReferenceNumberStr
    ) -> None:
        assert (
            validate_course_reference_number_str(valid_course_reference_number)
            == valid_course_reference_number
        )

    def test_course_reference_number_str_invalid(
        self, invalid_course_reference_number: CourseReferenceNumberStr
    ) -> None:
        with pytest.raises(ValueError):
            validate_course_reference_number_str(invalid_course_reference_number)

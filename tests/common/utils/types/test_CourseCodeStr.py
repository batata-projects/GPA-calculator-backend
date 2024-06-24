import pytest

from src.common.utils.types.CourseCodeStr import CourseCodeStr, validate_course_code_str


class TestCourseCodeStr:
    def test_course_code_str_successful(
        self, valid_course_code_str: CourseCodeStr
    ) -> None:
        assert validate_course_code_str(valid_course_code_str) == valid_course_code_str

    def test_course_code_str_invalid(
        self, invalid_course_code_str: CourseCodeStr
    ) -> None:
        with pytest.raises(ValueError):
            validate_course_code_str(invalid_course_code_str)

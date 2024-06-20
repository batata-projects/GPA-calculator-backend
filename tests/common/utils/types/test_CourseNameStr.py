import pytest

from src.common.utils.types.CourseNameStr import CourseNameStr, validate_course_name_str


class TestCourseNameStr:
    def test_course_name_str_successful(self, valid_course_name: CourseNameStr) -> None:
        assert validate_course_name_str(valid_course_name) == valid_course_name

    def test_course_name_str_invalid(self, invalid_course_name: CourseNameStr) -> None:
        with pytest.raises(ValueError):
            validate_course_name_str(invalid_course_name)

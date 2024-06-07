import pytest

from src.common.utils.types.CourseCodeStr import CourseCodeStr, validate_course_code


class TestCourseCodeStr:
    def test_course_code_str_successful(self, valid_course_code: CourseCodeStr):
        assert validate_course_code(valid_course_code) == valid_course_code

    def test_course_code_str_invalid(self, invalid_course_code: CourseCodeStr):
        with pytest.raises(ValueError):
            validate_course_code(invalid_course_code)

import pytest

from src.common.utils.types.CourseStr import CourseStr, validate_course_str


class TestCourseStr:
    @pytest.mark.parametrize("course_str", ["valid_course_str1", "valid_course_str2"])
    def test_course_str_successful(
        self, course_str: CourseStr, request: pytest.FixtureRequest
    ) -> None:
        course_str = request.getfixturevalue(course_str)
        assert validate_course_str(course_str) == course_str

    @pytest.mark.parametrize(
        "course_str",
        [
            "none_course_str",
            "invalid_course_str",
        ],
    )
    def test_course_str_invalid(
        self, course_str: CourseStr, request: pytest.FixtureRequest
    ) -> None:
        course_str = request.getfixturevalue(course_str)
        with pytest.raises(ValueError):
            validate_course_str(course_str)

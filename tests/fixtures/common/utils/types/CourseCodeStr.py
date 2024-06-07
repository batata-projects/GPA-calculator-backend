import pytest

from src.common.utils.types.CourseCodeStr import CourseCodeStr


@pytest.fixture
def valid_course_code() -> CourseCodeStr:
    return "202"


@pytest.fixture
def invalid_course_code() -> CourseCodeStr:
    return "invalid-course-code"

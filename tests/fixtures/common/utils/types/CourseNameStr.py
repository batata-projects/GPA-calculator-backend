import pytest

from src.common.utils.types import CourseNameStr


@pytest.fixture
def valid_course_name() -> CourseNameStr:
    return "COMP"


@pytest.fixture
def invalid_course_name() -> CourseNameStr:
    return "invalid-course-name"

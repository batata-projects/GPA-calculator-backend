import pytest

from src.common.utils.types import CourseCodeStr


@pytest.fixture
def valid_course_code_str() -> CourseCodeStr:
    return "230"


@pytest.fixture
def invalid_course_code_str() -> CourseCodeStr:
    return None  # type: ignore

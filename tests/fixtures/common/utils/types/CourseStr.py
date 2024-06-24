import pytest

from src.common.utils.types import CourseStr


@pytest.fixture
def valid_course_str1() -> CourseStr:
    return "EECE"


@pytest.fixture
def valid_course_str2() -> CourseStr:
    return "230"


@pytest.fixture
def none_course_str() -> None:
    return None


@pytest.fixture
def invalid_course_str() -> CourseStr:
    return "251w"

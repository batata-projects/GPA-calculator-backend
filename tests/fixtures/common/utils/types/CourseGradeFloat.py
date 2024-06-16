import pytest

from src.common.utils.types import CourseGradeFloat


@pytest.fixture
def valid_course_grade_float() -> CourseGradeFloat:
    return 2.7


@pytest.fixture
def invalid_course_grade_float() -> CourseGradeFloat:
    return 1.1

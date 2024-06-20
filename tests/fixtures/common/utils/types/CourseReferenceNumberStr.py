import pytest

from src.common.utils.types.CourseReferenceNumberStr import CourseReferenceNumberStr


@pytest.fixture
def valid_course_reference_number() -> CourseReferenceNumberStr:
    return "12345"


@pytest.fixture
def invalid_course_reference_number() -> CourseReferenceNumberStr:
    return "invalid-course-reference-number"

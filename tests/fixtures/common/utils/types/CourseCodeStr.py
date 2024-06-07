import pytest


@pytest.fixture
def valid_course_code():
    return "202"


@pytest.fixture
def invalid_course_code():
    return "invalid-course-code"

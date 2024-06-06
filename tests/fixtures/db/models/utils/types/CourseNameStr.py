import pytest


@pytest.fixture
def valid_course_name():
    return "COMP"


@pytest.fixture
def invalid_course_name():
    return "invalid-course-name"

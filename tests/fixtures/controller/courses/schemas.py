import pytest

from src.controller.courses import CourseRequest
from src.db.models import Course


@pytest.fixture
def course_request(course1: Course) -> CourseRequest:
    return CourseRequest(
        available_course_id=course1.available_course_id,
        user_id=course1.user_id,
        grade=course1.grade,
        passed=course1.passed,
    )

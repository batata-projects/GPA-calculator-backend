import pytest

from src.controller.available_courses import AvailableCourseRequest
from src.db.models import AvailableCourse


@pytest.fixture
def available_course_request(
    available_course1: AvailableCourse,
) -> AvailableCourseRequest:
    return AvailableCourseRequest(
        term_id=available_course1.term_id,
        name=available_course1.name,
        code=available_course1.code,
        credits=available_course1.credits,
        graded=available_course1.graded,
    )

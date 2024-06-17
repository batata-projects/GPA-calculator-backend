import pytest

from src.controller.courses import CourseResponse
from src.db.models import Course


class TestCourseResponse:
    def test_course_response_successful(self, course1: Course) -> None:
        course_response = CourseResponse(items=[course1])

        assert course_response.items == [course1]

    def test_course_response_empty(self) -> None:
        course_response = CourseResponse()

        assert course_response.items == []

    def test_course_multiple_courses(self, course1: Course, course2: Course) -> None:
        course_response = CourseResponse(items=[course1, course2])

        assert course_response.items == [course1, course2]

    def test_course_response_invalid_course(self) -> None:
        with pytest.raises(ValueError):
            CourseResponse(items=[{"name": "Course 1"}])  # type: ignore

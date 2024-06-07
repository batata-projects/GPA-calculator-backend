from unittest.mock import Mock
import pytest
import src.controller.available_courses.router as available_courses_router
from src.db.dao.available_course_dao import AvailableCourseDAO
from src.db.models.available_courses import AvailableCourse

class TestAvailableCourseRouter:
    def test_get_available_course_by_id(self, available_courses: list[AvailableCourse]):
        available_course = available_courses[0]
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.get_available_course_by_id.return_value = available_course
        available_course_router = available_courses_router.AvailableCourseRouter(available_course_dao)
        assert available_course_router.get_available_course_by_id(available_course.id) == available_course

from unittest.mock import Mock

from src.db.models.courses import Course


class TestCourses:
    def test_create_course(self, uuid4: Mock):
        course_id = str(uuid4())
        available_course_id = str(uuid4())
        user_id = str(uuid4())
        grade = 4.0
        passed = True

        course = Course(
            id=course_id,
            available_course_id=available_course_id,
            user_id=user_id,
            grade=grade,
            passed=passed,
        )

        assert course.id == course_id
        assert course.available_course_id == available_course_id
        assert course.user_id == user_id
        assert course.grade == grade
        assert course.passed == passed

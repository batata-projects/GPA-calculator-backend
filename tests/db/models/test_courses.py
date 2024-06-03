from unittest.mock import Mock

import pytest

from src.db.models.courses import Course


class TestCourse:
    def test_course_successful(self, uuid4: Mock):
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

    def test_course_no_id(self, uuid4: Mock):
        available_course_id = str(uuid4())
        user_id = str(uuid4())
        grade = 4.0
        passed = True

        course = Course(
            available_course_id=available_course_id,
            user_id=user_id,
            grade=grade,
            passed=passed,
        )

        assert course.id is None
        assert course.available_course_id == available_course_id
        assert course.user_id == user_id
        assert course.grade == grade
        assert course.passed == passed

    @pytest.mark.parametrize(
        "available_course_id, user_id, grade, passed",
        [
            (None, "uuid4", 4.0, True),
            ("uuid4", None, 4.0, True),
            ("uuid4", "uuid4", None, True),
            ("uuid4", "uuid4", 4.0, None),
        ],
    )
    def test_course_invalid_attribute(
        self,
        available_course_id,
        user_id,
        grade,
        passed,
        request: pytest.FixtureRequest,
    ):
        if available_course_id is not None:
            available_course_id = str(request.getfixturevalue(available_course_id))
        if user_id is not None:
            user_id = str(request.getfixturevalue(user_id))
        with pytest.raises(ValueError):
            Course(
                available_course_id=available_course_id,
                user_id=user_id,
                grade=grade,
                passed=passed,
            )

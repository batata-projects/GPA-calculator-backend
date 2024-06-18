from unittest.mock import Mock

import pytest

from src.common.utils.types import CourseGradeFloat, UuidStr
from src.db.models import Course


class TestCourse:
    def test_course_successful(self, valid_uuid: Mock) -> None:
        course_id = str(valid_uuid)
        available_course_id = str(valid_uuid)
        user_id = str(valid_uuid)
        grade = 4.0
        passed = True
        graded = True

        course = Course(
            id=course_id,
            available_course_id=available_course_id,
            user_id=user_id,
            grade=grade,
            passed=passed,
            graded=graded,
        )

        assert course.id == course_id
        assert course.available_course_id == available_course_id
        assert course.user_id == user_id
        assert course.grade == grade
        assert course.passed == passed
        assert course.graded == graded

    def test_course_no_id(self, valid_uuid: Mock) -> None:
        available_course_id = str(valid_uuid)
        user_id = str(valid_uuid)
        grade = 4.0
        passed = True
        graded = True

        course = Course(
            available_course_id=available_course_id,
            user_id=user_id,
            grade=grade,
            passed=passed,
            graded=graded,
        )

        assert course.id is None
        assert course.available_course_id == available_course_id
        assert course.user_id == user_id
        assert course.grade == grade
        assert course.passed == passed
        assert course.graded == graded

    def test_course_invalid_id(self, valid_uuid: Mock) -> None:
        course_id = "invalid"
        available_course_id = str(valid_uuid)
        user_id = str(valid_uuid)
        grade = 4.0
        passed = True
        graded = True

        with pytest.raises(ValueError):
            Course(
                id=course_id,
                available_course_id=available_course_id,
                user_id=user_id,
                grade=grade,
                passed=passed,
                graded=graded,
            )

    @pytest.mark.parametrize(
        "available_course_id, user_id, grade, passed, graded",
        [
            (None, "uuid4", 4.0, True, True),
            ("uuid4", None, 4.0, True, True),
            ("uuid4", "uuid4", 4.0, True, None),
        ],
    )
    def test_course_none_attribute(
        self,
        available_course_id: UuidStr,
        user_id: UuidStr,
        grade: CourseGradeFloat,
        passed: bool,
        graded: bool,
        request: pytest.FixtureRequest,
    ) -> None:
        if available_course_id is not None:
            available_course_id = str(
                getattr(request.getfixturevalue(available_course_id), "return_value")
            )
        if user_id is not None:
            user_id = str(getattr(request.getfixturevalue(user_id), "return_value"))
        with pytest.raises(ValueError):
            Course(
                available_course_id=available_course_id,
                user_id=user_id,
                grade=grade,
                passed=passed,
                graded=graded,
            )

    @pytest.mark.parametrize(
        "available_course_id, user_id, grade, passed, graded",
        [
            ("12345", "uuid4", 4.0, True, True),
            ("uuid4", "12345", 4.0, True, True),
            ("uuid4", "uuid4", -1, True, True),
            ("uuid4", "uuid4", 4.0, -1, True),
            ("uuid4", "uuid4", 4.0, True, -1),
        ],
    )
    def test_course_invalid_attribute(
        self,
        available_course_id: UuidStr,
        user_id: UuidStr,
        grade: CourseGradeFloat,
        passed: bool,
        graded: bool,
        request: pytest.FixtureRequest,
    ) -> None:
        if available_course_id == "uuid4":
            available_course_id = str(
                getattr(request.getfixturevalue(available_course_id), "return_value")
            )
        if user_id == "uuid4":
            user_id = str(getattr(request.getfixturevalue(user_id), "return_value"))
        with pytest.raises(ValueError):
            Course(
                available_course_id=available_course_id,
                user_id=user_id,
                grade=grade,
                passed=passed,
                graded=graded,
            )

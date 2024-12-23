from unittest.mock import Mock

import pytest
from pydantic import NonNegativeInt

from src.common.utils.types import CourseGradeFloat, CourseStr, TermInt, UuidStr
from src.db.models import Course


class TestCourse:
    def test_course_successful(self, uuid_generator: Mock) -> None:
        course_id = uuid_generator()
        user_id = uuid_generator()
        subject = "EECE"
        course_code = "230"
        term = 202310
        credits = 3
        grade = 4.3
        graded = True

        course = Course(
            id=course_id,
            user_id=user_id,
            subject=subject,
            course_code=course_code,
            term=term,
            credits=credits,
            grade=grade,
            graded=graded,
        )

        assert course.id == course_id
        assert course.user_id == user_id
        assert course.subject == subject
        assert course.course_code == course_code
        assert course.term == term
        assert course.credits == credits
        assert course.grade == grade
        assert course.graded == graded

    def test_course_no_id(self, uuid_generator: Mock) -> None:
        user_id = uuid_generator()
        subject = "EECE"
        course_code = "230"
        term = 202310
        credits = 3
        grade = 4.3
        graded = True

        course = Course(
            user_id=user_id,
            subject=subject,
            course_code=course_code,
            term=term,
            credits=credits,
            grade=grade,
            graded=graded,
        )

        assert course.user_id == user_id
        assert course.subject == subject
        assert course.course_code == course_code
        assert course.term == term
        assert course.credits == credits
        assert course.grade == grade
        assert course.graded == graded

    def test_course_invalid_id(
        self, uuid_generator: Mock, invalid_uuid: UuidStr
    ) -> None:
        course_id = invalid_uuid
        user_id = uuid_generator()
        subject = "EECE"
        course_code = "230"
        term = 202310
        credits = 3
        grade = 4.3
        graded = True

        with pytest.raises(ValueError):
            Course(
                id=course_id,
                user_id=user_id,
                subject=subject,
                course_code=course_code,
                term=term,
                credits=credits,
                grade=grade,
                graded=graded,
            )

    @pytest.mark.parametrize(
        "user_id, subject, course_code, term, credits, grade, graded",
        [
            (None, "EECE", "230", 202310, 3, 4.3, True),
            ("uuid_generator", None, "230", 202310, 3, 4.3, True),
            ("uuid_generator", "EECE", None, 202310, 3, 4.3, True),
            ("uuid_generator", "EECE", "230", None, 3, 4.3, True),
            ("uuid_generator", "EECE", "230", 202310, None, 4.3, True),
            ("uuid_generator", "EECE", "230", 202310, 3, 4.3, None),
        ],
    )
    def test_course_none_attribute(
        self,
        user_id: UuidStr,
        subject: CourseStr,
        course_code: CourseStr,
        term: TermInt,
        credits: NonNegativeInt,
        grade: CourseGradeFloat,
        graded: bool,
        request: pytest.FixtureRequest,
    ) -> None:
        if user_id is not None:
            user_id = request.getfixturevalue(user_id)()
        with pytest.raises(ValueError):
            Course(
                user_id=user_id,
                subject=subject,
                course_code=course_code,
                term=term,
                credits=credits,
                grade=grade,
                graded=graded,
            )

    @pytest.mark.parametrize(
        "term_name, year, expected",
        [
            ("Fall", 2023, 202310),
            ("Winter", 2023, 202315),
            ("Spring", 2023, 202320),
            ("Summer", 2023, 202330),
            ("Fall", 2023, 202310),
            ("Winter", 2023, 202315),
            ("Spring", 2023, 202320),
            ("Summer", 2023, 202330),
        ],
    )
    def test_convert_to_term_number_successful(
        self, term_name: str, year: int, expected: int
    ) -> None:
        assert Course.convert_to_term_number(term_name, year) == expected

    @pytest.mark.parametrize(
        "term_name, year",
        [
            ("Invalid", 2023),
            ("Fall", 0),
            ("Winter", 0),
            ("Spring", 0),
            ("Summer", 0),
        ],
    )
    def test_convert_to_term_number_invalid(self, term_name: str, year: int) -> None:
        with pytest.raises(ValueError):
            Course.convert_to_term_number(term_name, year)

    @pytest.mark.parametrize(
        "term_number, expected",
        [
            (202310, ("Fall", 2023)),
            (202315, ("Winter", 2023)),
            (202320, ("Spring", 2023)),
            (202330, ("Summer", 2023)),
        ],
    )
    def test_convert_to_term_name_successful(
        self, term_number: int, expected: tuple[str, int]
    ) -> None:
        assert Course.convert_to_term_name(term_number) == expected

    @pytest.mark.parametrize(
        "term_number",
        [
            0,
            202300,
            202340,
        ],
    )
    def test_convert_to_term_name_invalid(self, term_number: int) -> None:
        with pytest.raises(ValueError):
            Course.convert_to_term_name(term_number)

    def test_check_grade_and_graded_successful(self) -> None:
        values = {
            "graded": True,
            "grade": 4.3,
        }
        assert Course._check_grade_and_graded(values) == values

    def test_check_grade_and_graded_invalid(self) -> None:
        values = {
            "graded": False,
            "grade": 4.3,
        }
        with pytest.raises(ValueError):
            Course._check_grade_and_graded(values)

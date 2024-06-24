import pytest
from pydantic import NonNegativeInt

from src.common.utils.types import (
    CourseCodeStr,
    CourseGradeFloat,
    SubjectStr,
    TermInt,
    UuidStr,
)
from src.db.models import Course


class TestCourse:
    def test_course_successful(self, valid_uuid: UuidStr) -> None:
        course_id = valid_uuid
        user_id = valid_uuid
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

    def test_course_no_id(self, valid_uuid: UuidStr) -> None:
        user_id = valid_uuid
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
        self, valid_uuid: UuidStr, invalid_uuid: UuidStr
    ) -> None:
        course_id = invalid_uuid
        user_id = valid_uuid
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
            ("valid_uuid", None, "230", 202310, 3, 4.3, True),
            ("valid_uuid", "EECE", None, 202310, 3, 4.3, True),
            ("valid_uuid", "EECE", "230", None, 3, 4.3, True),
            ("valid_uuid", "EECE", "230", 202310, None, 4.3, True),
            ("valid_uuid", "EECE", "230", 202310, 3, 4.3, None),
        ],
    )
    def test_course_none_attribute(
        self,
        user_id: UuidStr,
        subject: SubjectStr,
        course_code: CourseCodeStr,
        term: TermInt,
        credits: NonNegativeInt,
        grade: CourseGradeFloat,
        graded: bool,
        request: pytest.FixtureRequest,
    ) -> None:
        if user_id is not None:
            user_id = request.getfixturevalue(user_id)
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

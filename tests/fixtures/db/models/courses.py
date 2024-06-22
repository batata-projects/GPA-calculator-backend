from unittest.mock import Mock

import pytest

from src.db.models import Course


@pytest.fixture
def courses(valid_uuid: Mock) -> list[Course]:
    return [
        Course(
            id=valid_uuid,
            user_id=valid_uuid,
            subject="EECE",
            course_code="230",
            term=202310,
            credits=3,
            grade=4.3,
            graded=True,
        ),
        Course(
            id=valid_uuid,
            user_id=valid_uuid,
            subject="FEAA",
            course_code="200",
            term=202310,
            credits=3,
            grade=1,
            graded=False,
        ),
    ]


@pytest.fixture
def course1(courses: list[Course]) -> Course:
    return courses[0]


@pytest.fixture
def course2(courses: list[Course]) -> Course:
    return courses[1]


@pytest.fixture
def courses_same_user_id(
    courses: list[Course],
) -> list[Course]:
    courses[1].user_id = courses[0].user_id
    return courses


@pytest.fixture
def courses_same_grade(
    courses: list[Course],
) -> list[Course]:
    courses[1].grade = courses[0].grade
    return courses

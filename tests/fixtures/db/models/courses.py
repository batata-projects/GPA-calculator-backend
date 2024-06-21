from unittest.mock import Mock

import pytest

from src.db.models import Course


@pytest.fixture
def courses(valid_uuid: Mock) -> list[Course]:
    return [
        Course(
            id=str(valid_uuid),
            available_course_id=str(valid_uuid),
            user_id=str(valid_uuid),
            grade=4.0,
            graded=True,
        ),
        Course(
            id=str(valid_uuid),
            available_course_id=str(valid_uuid),
            user_id=str(valid_uuid),
            grade=2.0,
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
def courses_same_available_course_id(
    courses: list[Course],
) -> list[Course]:
    courses[1].available_course_id = courses[0].available_course_id
    return courses


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

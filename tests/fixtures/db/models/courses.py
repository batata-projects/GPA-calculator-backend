from unittest.mock import Mock

import pytest

from src.db.models import Course


@pytest.fixture
def courses(uuid4: Mock) -> list[Course]:
    return [
        Course(
            id=str(uuid4()),
            available_course_id=str(uuid4()),
            user_id=str(uuid4()),
            grade=4.0,
            passed=True,
        ),
        Course(
            id=str(uuid4()),
            available_course_id=str(uuid4()),
            user_id=str(uuid4()),
            grade=2.0,
            passed=False,
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

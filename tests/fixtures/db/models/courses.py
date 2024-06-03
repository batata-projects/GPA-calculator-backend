from unittest.mock import Mock

import pytest

from src.db.models.courses import Course


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
def courses_same_available_course_id(
    course: list[Course],
) -> list[Course]:
    course[1].available_course_id = course[0].available_course_id
    return course


@pytest.fixture
def courses_same_user_id(
    course: list[Course],
) -> list[Course]:
    course[1].user_id = course[0].user_id
    return course


@pytest.fixture
def courses_same_grade(
    course: list[Course],
) -> list[Course]:
    course[1].grade = course[0].grade
    return course


@pytest.fixture
def courses_same_passed(
    course: list[Course],
) -> list[Course]:
    course[1].passed = course[0].passed
    return course

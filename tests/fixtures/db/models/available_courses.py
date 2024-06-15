from typing import Any
from unittest.mock import Mock

import pytest

from src.db.models import AvailableCourse


@pytest.fixture
def available_courses(uuid4: Mock) -> list[AvailableCourse]:
    return [
        AvailableCourse(
            id=str(uuid4()),
            term_id=str(uuid4()),
            name="PHYS",
            code="210L",
            credits=1,
            graded=True,
        ),
        AvailableCourse(
            id=str(uuid4()),
            term_id=str(uuid4()),
            name="FEAA",
            code="200",
            credits=3,
            graded=False,
        ),
    ]


@pytest.fixture
def available_course1(available_courses: list[AvailableCourse]) -> AvailableCourse:
    return available_courses[0]


@pytest.fixture
def available_course2(available_courses: list[AvailableCourse]) -> AvailableCourse:
    return available_courses[1]


@pytest.fixture
def available_courses_same_course_name(
    available_courses: list[AvailableCourse],
) -> list[AvailableCourse]:
    available_courses[1].name = available_courses[0].name
    return available_courses


@pytest.fixture
def available_courses_same_credits(
    available_courses: list[AvailableCourse],
) -> list[AvailableCourse]:
    available_courses[1].credits = available_courses[0].credits
    return available_courses


@pytest.fixture
def available_courses_same_terms(
    available_courses: list[AvailableCourse],
) -> list[AvailableCourse]:
    available_courses[1].term_id = available_courses[0].term_id
    return available_courses


@pytest.fixture
def available_courses_same_graded(
    available_courses: list[AvailableCourse],
) -> list[AvailableCourse]:
    available_courses[1].graded = available_courses[0].graded
    return available_courses


@pytest.fixture
def available_courses_data(uuid4: Mock) -> list[dict[str, Any]]:
    return [
        {
            "id": str(uuid4()),
            "term_id": str(uuid4()),
            "name": "PHYS",
        },
        {
            "code": "200",
            "credits": 3,
            "graded": False,
        },
        {
            "term_id": str(uuid4()),
            "credits": 1,
        },
    ]


@pytest.fixture
def invalid_available_course_data(uuid4: Mock) -> list[dict[str, Any]]:
    return [
        {
            "id": str(uuid4()),
            "term_id": 123,
            "name": "PHYS",
        },
        {
            "name": "PHYS",
            "code": "20",
            "credits": 3,
            "graded": False,
        },
        {
            "id": str(uuid4()),
            "term_id": str(uuid4()),
            "name": "PHYS",
            "code": "200",
            "credits": 3,
            "graded": -1,
        },
    ]

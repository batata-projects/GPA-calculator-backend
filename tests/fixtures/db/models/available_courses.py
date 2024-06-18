from typing import Any
from unittest.mock import Mock

import pytest

from src.db.models import AvailableCourse


@pytest.fixture
def available_courses(valid_uuid: Mock) -> list[AvailableCourse]:
    return [
        AvailableCourse(
            id=str(valid_uuid),
            term_id=str(valid_uuid),
            name="PHYS",
            code="210L",
            credits=1,
        ),
        AvailableCourse(
            id=str(valid_uuid),
            term_id=str(valid_uuid),
            name="FEAA",
            code="200",
            credits=3,
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
def available_courses_data(valid_uuid: Mock) -> list[dict[str, Any]]:
    return [
        {
            "id": str(valid_uuid),
            "term_id": str(valid_uuid),
            "name": "PHYS",
        },
        {
            "code": "200",
            "credits": 3,
        },
        {
            "term_id": str(valid_uuid),
            "credits": 1,
        },
    ]


@pytest.fixture
def invalid_available_course_data(valid_uuid: Mock) -> list[dict[str, Any]]:
    return [
        {
            "id": str(valid_uuid),
            "term_id": 123,
            "name": "PHYS",
        },
        {
            "name": "PHYS",
            "code": "20",
            "credits": 3,
        },
        {
            "id": str(valid_uuid),
            "term_id": str(valid_uuid),
            "name": "SUBJECT",
            "code": "200",
            "credits": 3,
        },
    ]

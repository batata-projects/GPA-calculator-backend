from unittest.mock import Mock

import pytest

from src.db.models import Term


@pytest.fixture
def terms(valid_uuid: Mock) -> list[Term]:
    return [
        Term(
            id=str(valid_uuid),
            name="Fall 2022 - 2023",
        ),
        Term(
            id=str(valid_uuid),
            name="Spring 2023 - 2024",
        ),
    ]


@pytest.fixture
def term1(terms: list[Term]) -> Term:
    return terms[0]


@pytest.fixture
def term2(terms: list[Term]) -> Term:
    return terms[1]


@pytest.fixture
def terms_same_name(
    terms: list[Term],
) -> list[Term]:
    terms[1].name = terms[0].name
    return terms

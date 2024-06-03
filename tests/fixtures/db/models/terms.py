from unittest.mock import Mock

import pytest

from src.db.models.terms import Term


@pytest.fixture
def terms(uuid4: Mock) -> list[Term]:
    return [
        Term(
            id=str(uuid4()),
            name="Fall 2022 - 2023",
        ),
        Term(
            id=str(uuid4()),
            name="Spring 2023 - 2024",
        ),
    ]


@pytest.fixture
def terms_same_name(
    terms: list[Term],
) -> list[Term]:
    terms[1].name = terms[0].name
    return terms

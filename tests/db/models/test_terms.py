from unittest.mock import Mock

import pytest

from src.db.models import Term


class TestTerm:
    def test_term_successful(self, uuid4: Mock) -> None:
        term_id = str(uuid4())
        name = "Fall 2022 - 2023"

        term = Term(
            id=term_id,
            name=name,
        )

        assert term.id == term_id
        assert term.name == name

    def test_term_no_id(self) -> None:
        name = "Fall 2022 - 2023"

        term = Term(
            name=name,
        )

        assert term.id is None
        assert term.name == name

    def test_term_invalid_id(self) -> None:
        term_id = "invalid"
        name = "Fall 2022 - 2023"

        with pytest.raises(ValueError):
            Term(
                id=term_id,
                name=name,
            )

    def test_term_invalid_str(self) -> None:
        name = "Fall 2022-2023"

        with pytest.raises(ValueError):
            Term(
                name=name,
            )

    def test_term_invalid_attribute(self) -> None:
        with pytest.raises(ValueError):
            Term(
                name=None,  # type: ignore
            )

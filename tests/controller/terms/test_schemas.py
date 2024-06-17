import pytest

from src.controller.terms import TermResponse
from src.db.models import Term


class TestTermResponse:
    def test_term_response_successful(self, term1: Term) -> None:
        term_response = TermResponse(items=[term1])

        assert term_response.items == [term1]

    def test_term_response_empty(self) -> None:
        term_response = TermResponse()

        assert term_response.items == []

    def test_term_multiple_terms(self, term1: Term, term2: Term) -> None:
        term_response = TermResponse(items=[term1, term2])

        assert term_response.items == [term1, term2]

    def test_term_response_invalid_term(self) -> None:
        with pytest.raises(ValueError):
            TermResponse(items=[{"name": "Term 1"}])  # type: ignore

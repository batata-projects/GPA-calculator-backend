import pytest

from src.controller.terms.schemas import TermResponse
from src.db.models.terms import Term


class TestTermResponse:
    def test_term_response_successful(self, term1: Term):
        term_response = TermResponse(terms=[term1])

        assert term_response.terms == [term1]

    def test_term_response_empty(self):
        term_response = TermResponse()

        assert term_response.terms == []

    def test_term_multiple_terms(self, term1: Term, term2: Term):
        term_response = TermResponse(terms=[term1, term2])

        assert term_response.terms == [term1, term2]

    def test_term_response_invalid_term(self):
        with pytest.raises(ValueError):
            TermResponse(terms=[{"name": "Term 1"}])  # type: ignore

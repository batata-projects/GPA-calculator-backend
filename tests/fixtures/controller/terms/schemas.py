import pytest

from src.controller.terms import TermRequest
from src.db.models import Term


@pytest.fixture
def term_request(term1: Term) -> TermRequest:
    return TermRequest(
        name=term1.name,
    )

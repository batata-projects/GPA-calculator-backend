from src.controller.schemas.terms import TermQuery


def test_term_query() -> None:
    query = TermQuery()
    assert query is not None
    assert query.model_dump() == {
        "name": None,
    }

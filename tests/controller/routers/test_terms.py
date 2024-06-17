from src.controller.routers.terms import terms_router


def test_terms_router() -> None:
    assert terms_router.prefix == "/terms"
    assert terms_router.tags == ["Terms"]

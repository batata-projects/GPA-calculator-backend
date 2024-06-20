from src.core.scraping.terms import TermsScraper


class TestTermsScraper:
    def test_fetch_terms(self) -> None:
        TS = TermsScraper(None)
        TS.fetch_terms
        assert True
        ...

    def test_create_terms(self) -> None:
        TS = TermsScraper(None)
        TS.create_terms
        assert True
        ...

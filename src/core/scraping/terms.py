import requests
from fastapi import HTTPException, status

from src.db.dao import TermDAO
from src.db.models import Term


class TermsScraper:
    def __init__(self, term_dao: TermDAO, offset: int = 1, max: int = 100):
        self.base_url = "https://sturegss.aub.edu.lb/StudentRegistrationSsb/ssb/classSearch/getTerms?offset={offset}&max={max}"
        self.offset = offset
        self.max = max
        self.term_dao = term_dao

    def fetch_terms(self) -> list[Term]:
        url = self.base_url.format(
            offset=self.offset,
            max=self.max,
        )
        data = []
        response = requests.request("GET", url)
        if response.status_code != status.HTTP_200_OK:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to get terms",
            )
        response_data = response.json()
        for term in response_data:
            try:
                data.append(Term.convert_from_sis_term(term["code"]))
            except ValueError:
                continue
        return data

    def create_terms(self) -> list[Term]:
        terms = self.fetch_terms()
        for i, term in enumerate(terms):
            _term = self.term_dao.get_by_query(name=term.name)
            if _term and len(_term) > 0:
                terms[i] = _term[0]
            else:
                created_term = self.term_dao.create({"name": term.name})
                if created_term:
                    terms[i] = created_term
        return terms

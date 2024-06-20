from src.core.scraping.available_courses import AvailableCoursesScraper
from src.core.scraping.terms import TermsScraper
from src.db.dependencies import (
    get_scrapper_available_courses_dao,
    get_scrapper_terms_dao,
)


term_dao = get_scrapper_terms_dao()
available_courses_dao = get_scrapper_available_courses_dao()


TS = TermsScraper(term_dao)
TS.create_terms()

ACS = AvailableCoursesScraper(term_dao, available_courses_dao)

terms = ACS.term_dao.get_by_query()

ACS.create_available_courses(terms)

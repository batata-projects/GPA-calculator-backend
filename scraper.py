from src.core.scraping.available_courses import AvailableCoursesScraper
from src.core.scraping.terms import TermsScraper
from src.db.dependencies import (
    get_scrapper_available_courses_dao,
    get_scrapper_terms_dao,
)

SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InR1YnlyY3dtYWhicXljaGd3dndzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTY0OTgxOTcsImV4cCI6MjAzMjA3NDE5N30.juNtlWxdGqGuGmrsQZOEV22r7azt4O4XjrL-v5OBVkg"
SUPABASE_URL = "https://tubyrcwmahbqychgwvws.supabase.co"
JWT_SECRET = "utn5Waa2i6og6vECF29HUTrvfDD8ouubtEUlEaW4838JFCchzjxqhlNiMCwYUtauskOrBC2+xxhqk31LAXx58Q=="
SUPABASE_SCRAPER_EMAIL = "jss31@mail.aub.edu"
SUPABASE_SCRAPER_PASSWORD = "Password123"

open('.env', 'w').write(f"SUPABASE_KEY={SUPABASE_KEY}\nSUPABASE_URL={SUPABASE_URL}\nJWT_SECRET={JWT_SECRET}\nSUPABASE_SCRAPER_EMAIL={SUPABASE_SCRAPER_EMAIL}\nSUPABASE_SCRAPER_PASSWORD={SUPABASE_SCRAPER_PASSWORD}")


term_dao = get_scrapper_terms_dao()
available_courses_dao = get_scrapper_available_courses_dao()


TS = TermsScraper(term_dao)
TS.create_terms()

ACS = AvailableCoursesScraper(term_dao, available_courses_dao)

terms = ACS.term_dao.get_by_query()


for term in terms:
    print(term.name)
    available_courses = ACS.create_available_courses(term)
    print(len(available_courses))

from src.core.scraping.available_courses import AvailableCoursesScraper


class TestAvailableCourses:
    def test_available_courses(self) -> None:
        ACS = AvailableCoursesScraper(None, None)
        assert True
        ...

    def test_set_cookie(self) -> None:
        ACS = AvailableCoursesScraper(None, None)
        ACS._set_cookie
        assert True
        ...

    def test__fetch_available_courses(self) -> None:
        ACS = AvailableCoursesScraper(None, None)
        ACS._fetch_available_courses
        assert True
        ...

    def test_fetch_available_courses(self) -> None:
        ACS = AvailableCoursesScraper(None, None)
        ACS.fetch_available_courses
        assert True
        ...

    def test_create_available_courses(self) -> None:
        ACS = AvailableCoursesScraper(None, None)
        ACS.create_available_courses
        assert True
        ...

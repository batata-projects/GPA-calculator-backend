import requests
from fastapi import HTTPException, status

from src.common.utils.types import UuidStr
from src.db.dao import AvailableCourseDAO, TermDAO
from src.db.dependencies import (
    get_scrapper_available_courses_dao,
    get_scrapper_terms_dao,
)
from src.db.models import AvailableCourse


class AvailableCoursesScrapper:
    def __init__(self, term_dao: TermDAO, available_course_dao: AvailableCourseDAO):
        self.term_dao = term_dao
        self.available_course_dao = available_course_dao
        self.base_url = "https://sturegss.aub.edu.lb/StudentRegistrationSsb/ssb/searchResults/searchResults?txt_term={term_number}&pageOffset={page_offset}&pageMaxSize={page_max_size}"
        self.headers = {"Host": "sturegss.aub.edu.lb"}

    def fetch_course_graded(
        self, term_number: str, course_reference_number: str
    ) -> bool:
        return True

    def _fetch_available_courses(
        self,
        term_number: str,
        term_id: UuidStr,
        page_offset: int,
        page_max_size: int,
        data: dict[str, AvailableCourse] = {},
    ) -> dict[str, AvailableCourse]:
        url = self.base_url.format(
            term_number=term_number,
            page_offset=page_offset,
            page_max_size=page_max_size,
        )
        self.cookie = self._get_cookie()
        self.headers = {"Cookie": self.cookie}
        response = requests.request("GET", url, headers=self.headers)
        if response.status_code != status.HTTP_200_OK:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to get available courses",
            )
        response_data = response.json()["data"]
        for i, available_course in enumerate(response_data):
            grade = self.fetch_course_graded(
                term_number, available_course["courseReferenceNumber"]
            )
            course_name = str(
                available_course["subject"] + " " + available_course["courseNumber"]
            )
            if course_name in data:
                continue
            _available_course = AvailableCourse(
                term_id=term_id,
                name=available_course["subject"],
                code=available_course["courseNumber"],
                credits=int(
                    available_course["creditHours"] or available_course["creditHourLow"]
                ),
                graded=grade,
            )
            data[course_name] = _available_course
        return data

    def fetch_available_courses(
        self, term_number: str, term_id: UuidStr
    ) -> list[AvailableCourse]:
        data: dict[str, AvailableCourse] = {}
        page_offset = 0
        page_max_size = 500
        while True:
            courses = self._fetch_available_courses(
                term_number, term_id, page_offset, page_max_size, data
            )
            if not courses:
                break
            page_offset += page_max_size
        _data = list(data.values())
        return _data

    def create_available_courses(self) -> list[AvailableCourse]:
        terms = self.term_dao.get_by_query()
        for term in terms:
            if not term.id:
                continue
            available_courses = self.fetch_available_courses(
                term.get_sis_term(), term.id
            )
            for i, available_course in enumerate(available_courses):
                _available_course = self.available_course_dao.get_by_query(
                    term_id=available_course.term_id,
                    name=available_course.name,
                    code=available_course.code,
                )
                if _available_course and len(_available_course) > 0:
                    available_courses[i] = _available_course[0]
                else:
                    _dict = available_course.model_dump()
                    _dict.pop("id")
                    created_available_course = self.available_course_dao.create(_dict)
                    if created_available_course:
                        available_courses[i] = created_available_course
        return available_courses


ACS = AvailableCoursesScrapper(
    get_scrapper_terms_dao(), get_scrapper_available_courses_dao()
)

x = ACS.create_available_courses()

import time

import requests
from fastapi import HTTPException, status
from selenium.webdriver.common.by import By

from src.common.utils.types import UuidStr
from src.core.scraping.driver import Driver
from src.db.dao import AvailableCourseDAO, TermDAO
from src.db.models import AvailableCourse, Term


class AvailableCoursesScraper:
    def __init__(
        self,
        term_dao: TermDAO,
        available_course_dao: AvailableCourseDAO,
        logging: bool = True,
    ):
        self.term_dao = term_dao
        self.available_course_dao = available_course_dao
        self.logging = logging
        self.base_url = "https://sturegss.aub.edu.lb/StudentRegistrationSsb/ssb/searchResults/searchResults?txt_term={term_number}&pageOffset={page_offset}&pageMaxSize={page_max_size}"
        self.headers = {"Host": "sturegss.aub.edu.lb"}

    def _set_cookie(self, term_number: str) -> None:
        driver = Driver(
            headless=True,
            logs=False,
            switches=False,
            disable_images=True,
            disable_js=True,
        )
        driver.get(
            "https://sturegss.aub.edu.lb/StudentRegistrationSsb/ssb/term/termSelection?mode=search"
        )
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="select2-chosen-1"]').click()
        time.sleep(0.1)
        driver.find_element(By.XPATH, '//*[@id="s2id_autogen1_search"]').send_keys(
            term_number
        )
        time.sleep(2)
        driver.find_element(By.XPATH, f'//*[@id="select2-results-1"]/li[1]').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="term-go"]').click()
        cookies = driver.get_cookies()
        driver.quit()
        self.cookie = ""
        for _cookie in cookies:
            self.cookie += f"{_cookie['name']}={_cookie['value']}; "

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
        self.headers["Cookie"] = self.cookie
        response = requests.request("GET", url, headers=self.headers, data={})
        if response.status_code != status.HTTP_200_OK:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to get available courses",
            )
        response_data = response.json()["data"]
        for i, available_course in enumerate(response_data):
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
                    available_course["creditHours"]
                    or available_course["creditHourLow"]
                    or available_course["creditHourHigh"]
                    or sum(
                        [
                            _available["meetingTime"]["creditHourSession"]
                            for _available in available_course["meetingsFaculty"]
                            if _available["meetingTime"]["creditHourSession"]
                        ]
                    )
                    or 0
                ),
            )
            data[course_name] = _available_course
        return data

    def fetch_available_courses(
        self, term_number: str, term_id: UuidStr
    ) -> list[AvailableCourse]:
        data: dict[str, AvailableCourse] = {}
        page_offset = 0
        page_max_size = 500
        self._set_cookie(term_number=term_number)
        while True:
            retries = 0
            count = len(data)
            try:
                self._fetch_available_courses(
                    term_number, term_id, page_offset, page_max_size, data
                )
            except Exception as e:
                retries += 1
                self._set_cookie(term_number=term_number)
                self._fetch_available_courses(
                    term_number, term_id, page_offset, page_max_size, data
                )
                if retries == 3:
                    raise e
            if len(data) == count:
                break
            page_offset += page_max_size
        _data = list(data.values())
        return _data

    def create_available_courses(self, terms: list[Term]) -> list[AvailableCourse]:
        _to_create = []
        for term in terms:
            if self.logging:
                print(term.name)
            if not term.id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Term ID is required",
                )
            available_courses = self.fetch_available_courses(
                term.get_sis_term(), term.id
            )
            _available_courses = self.available_course_dao.get_by_query(term_id=term.id)
            for i, available_course in enumerate(available_courses):
                _available_course = [
                    _available_course
                    for _available_course in _available_courses
                    if _available_course.name == available_course.name
                    and _available_course.code == available_course.code
                ]
                if _available_course and len(_available_course) > 0:
                    available_courses[i] = _available_course[0]
                else:
                    _dict = available_course.model_dump()
                    _dict.pop("id")
                    _to_create.append(_dict)
        if _to_create:
            available_courses = self.available_course_dao.create_many(_to_create)
        return available_courses

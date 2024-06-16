from typing import Any
from unittest.mock import Mock

import pytest
from pydantic import NonNegativeInt

from src.common.utils.types import CourseCodeStr, CourseNameStr, UuidStr
from src.db.models import AvailableCourse


class TestAvailableCourse:
    def test_available_course_successful(self, valid_uuid: Mock) -> None:
        available_course_id = str(valid_uuid)
        terms_id = str(valid_uuid)
        name = "EECE"
        code = "230"
        credits = 3
        graded = True

        availableCourse = AvailableCourse(
            id=available_course_id,
            term_id=terms_id,
            name=name,
            code=code,
            credits=credits,
            graded=graded,
        )

        assert availableCourse.id == available_course_id
        assert availableCourse.term_id == terms_id
        assert availableCourse.name == name
        assert availableCourse.code == code
        assert availableCourse.credits == credits
        assert availableCourse.graded == graded

    def test_available_course_no_id(self, valid_uuid: Mock) -> None:
        terms_id = str(valid_uuid)
        name = "EECE"
        code = "230"
        credits = 3
        graded = True

        availableCourse = AvailableCourse(
            term_id=terms_id, name=name, code=code, credits=credits, graded=graded
        )

        assert availableCourse.id is None
        assert availableCourse.term_id == terms_id
        assert availableCourse.name == name
        assert availableCourse.code == code
        assert availableCourse.credits == credits
        assert availableCourse.graded == graded

    @pytest.mark.parametrize(
        "terms_id, name, code, credits, graded",
        [
            (None, "EECE", "230", 3, True),
            ("uuid4", None, "230", 3, True),
            ("uuid4", "EECE", None, 3, True),
            ("uuid4", "EECE", "230", None, True),
            ("uuid4", "EECE", "230", 3, None),
        ],
    )
    def test_available_course_none_attribute(
        self,
        terms_id: UuidStr,
        name: CourseNameStr,
        code: CourseCodeStr,
        credits: NonNegativeInt,
        graded: bool,
        request: pytest.FixtureRequest,
    ) -> None:
        if terms_id is not None:
            terms_id = str(getattr(request.getfixturevalue(terms_id), "return_value"))
        with pytest.raises(ValueError):
            AvailableCourse(
                term_id=terms_id, name=name, code=code, credits=credits, graded=graded
            )

    @pytest.mark.parametrize(
        "terms_id, name, code, credits, graded",
        [
            ("12345", "EECE", "230", 3, True),
            ("uuid4", "Electrical", "230", 3, True),
            ("uuid4", "EECE", "L12", 3, True),
            ("uuid4", "EECE", "230", 3.5, True),
            ("uuid4", "EECE", "230", 3, -1),
        ],
    )
    def test_available_course_invalid_attribute(
        self,
        terms_id: UuidStr,
        name: CourseNameStr,
        code: CourseCodeStr,
        credits: NonNegativeInt,
        graded: bool,
        request: pytest.FixtureRequest,
    ) -> None:
        if terms_id == "uuid4":
            terms_id = str(getattr(request.getfixturevalue(terms_id), "return_value"))
        with pytest.raises(ValueError):
            AvailableCourse(
                term_id=terms_id, name=name, code=code, credits=credits, graded=graded
            )

    def test_model_validate_partial_invalid(
        self, invalid_available_course_data: list[dict[str, Any]]
    ) -> None:
        for data in invalid_available_course_data:
            with pytest.raises(Exception):
                AvailableCourse.model_validate_partial(data)

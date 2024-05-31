from unittest.mock import Mock

import pytest

from src.db.models.available_courses import AvailableCourse


class TestAvailableCourse:
    def test_available_course_successful(self, uuid4: Mock):
        available_course_id = str(uuid4())
        terms_id = str(uuid4())
        name = "EECE"
        code = "230"
        credits = 3
        graded = True

        availableCourse = AvailableCourse(
            id=available_course_id,
            terms_id=terms_id,
            name=name,
            code=code,
            credits=credits,
            graded=graded,
        )

        assert availableCourse.id == available_course_id
        assert availableCourse.terms_id == terms_id
        assert availableCourse.name == name
        assert availableCourse.code == code
        assert availableCourse.credits == credits
        assert availableCourse.graded == graded

    def test_available_course_no_id(self, uuid4: Mock):
        terms_id = str(uuid4())
        name = "EECE"
        code = "230"
        credits = 3
        graded = True

        availableCourse = AvailableCourse(
            terms_id=terms_id, name=name, code=code, credits=credits, graded=graded
        )

        assert availableCourse.id is None
        assert availableCourse.terms_id == terms_id
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
    def test_available_course_invalid_attribute(
        self, terms_id, name, code, credits, graded, request: pytest.FixtureRequest
    ):
        if terms_id is not None:
            terms_id = str(request.getfixturevalue(terms_id))
        with pytest.raises(ValueError):
            AvailableCourse(
                terms_id=terms_id, name=name, code=code, credits=credits, graded=graded
            )

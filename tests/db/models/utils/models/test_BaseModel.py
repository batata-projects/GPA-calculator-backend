import pytest

from src.db.models.available_courses import AvailableCourse
from src.db.models.courses import Course
from src.db.models.terms import Term
from src.db.models.users import User
from src.db.models.utils.models.BaseModel import BaseModel


class TestBaseModel:
    # TODO: Add test for model_validate_partial
    @pytest.mark.parametrize(
        "_class, data",
        [
            (AvailableCourse, "available_courses"),
            (Course, "courses"),
            (Term, "terms"),
            (User, "users"),
        ],
    )
    def test_model_validate_partial(
        self, _class: BaseModel, data, request: pytest.FixtureRequest
    ):
        item: BaseModel = request.getfixturevalue(data)[0]
        data = item.model_dump()
        for key in data:
            _data = data.copy()
            del _data[key]
            _class.model_validate_partial(_data)

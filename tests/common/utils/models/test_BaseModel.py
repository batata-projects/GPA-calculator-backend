import pytest

from src.common.utils.models.BaseModel import BaseModel
from src.db.models.available_courses import AvailableCourse
from src.db.models.courses import Course
from src.db.models.terms import Term
from src.db.models.users import User


class TestBaseModel:
    @pytest.mark.parametrize(
        "_class, model",
        [
            (AvailableCourse, "available_courses"),
            (Course, "courses"),
            (Term, "terms"),
            (User, "users"),
        ],
    )
    def test_model_validate_partial(
        self, _class: BaseModel, model: str, request: pytest.FixtureRequest
    ) -> None:
        item: BaseModel = request.getfixturevalue(model)[0]
        data = item.model_dump()
        for key in data:
            _data = data.copy()
            del _data[key]
            _class.model_validate_partial(_data)

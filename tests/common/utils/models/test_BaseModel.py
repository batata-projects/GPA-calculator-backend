import pytest

from src.db.models import AvailableCourse, BaseModel, Course, Term, User


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

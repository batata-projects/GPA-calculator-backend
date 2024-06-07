from typing import Any

import pytest
from src.db.models.available_courses import AvailableCourse
from src.db.models.courses import Course
from src.db.models.terms import Term
from src.db.models.users import User
from src.db.models.utils.data.ValidData import ValidData

class TestBaseModel:
    @pytest.mark.parametrize(
        "_class, partial_data",
        [
            (AvailableCourse, {"name": ValidData.AvailableCourse.name}),
            (Course, {"grade": ValidData.Course.grade, "passed": ValidData.Course.passed}),
            (Term, {}),
            (User, {"email": ValidData.User.email, "username": ValidData.User.username}),
        ],
    )
    def test_model_validate_partial(self, _class, partial_data, request: pytest.FixtureRequest):
        _class = getattr(_class, "__name__")
        validated_data = _class.model_validate_partial(request.getfixturevalue(partial_data))
        
        # assert that the attributes that aren't in partial_data are set to their values in ValidData
        # assert that the attributes that are in partial_data are set to their values in partial_data
        for field in _class.model_fields:
            if field not in partial_data:
                assert getattr(validated_data, field) == getattr(ValidData.__dict__[f"{_class}.{field}"], field)
            else:
                assert getattr(validated_data, field) == partial_data[field]
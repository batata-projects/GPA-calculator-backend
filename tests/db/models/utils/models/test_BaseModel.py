from typing import Any

import pytest
from src.db.models.available_courses import AvailableCourse
from src.db.models.courses import Course
from src.db.models.terms import Term
from src.db.models.users import User
from src.db.models.utils.data.ValidData import ValidData

class TestBaseModel:
    # TODO: Add test for model_validate_partial
    @pytest.mark.parametrize(
        "_class, method_name, method_args",
        [
            ("AvailableCourse", "model_validate_partial", "{'name': ValidData.AvailableCourse.name}"),
            ("Course", "model_validate_partial", "{'grade': ValidData.Course.grade, 'passed': ValidData.Course.passed}"),
            ("Term", "model_validate_partial", "{'id': ValidData.Term.id}"),
            ("User", "model_validate_partial", "{'username': ValidData.User.username}"),
        ],
    )
    def test_model_validate_partial(self, _class, method_name, method_args):
        cls = globals()[_class]
        method = getattr(cls, method_name)
        method_args = eval(method_args)
        validated_data = method(method_args)
        # assert that the validated_data returned is correct
        # i.e. the data that was not provided in the method_args should be the default value
        for field in cls.model_fields.keys():
            if field in method_args:
                assert validated_data.__dict__[field] == method_args[field]
            else:
                assert validated_data.__dict__[field] == ValidData.__dict__[f"{_class}.{field}"]

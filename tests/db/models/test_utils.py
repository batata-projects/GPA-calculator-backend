import pytest
from pydantic import EmailStr

from src.db.models.utils import (  # noqa: F401
    validate_course_code,
    validate_course_name,
    validate_email_domain,
    validate_term_str,
    validate_uuid,
)


class TestUtils:
    @pytest.mark.parametrize(
        "function_name, function_args",
        [
            ("validate_uuid", "valid_uuid"),
            ("validate_email_domain", "valid_email"),
            ("validate_term_str", "valid_term"),
            ("validate_course_name", "valid_course_name"),
            ("validate_course_code", "valid_course_code"),
        ],
    )
    def test_validate_successful(
        self, function_name, function_args, request: pytest.FixtureRequest
    ):
        func = globals()[function_name]
        assert func(request.getfixturevalue(function_args)) == request.getfixturevalue(
            function_args
        )

    @pytest.mark.parametrize(
        "function_name, function_args",
        [
            ("validate_uuid", "invalid_uuid"),
            ("validate_email_domain", "invalid_email"),
            ("validate_email_domain", "invalid_domain"),
            ("validate_term_str", "invalid_term"),
            ("validate_course_name", "invalid_course_name"),
            ("validate_course_code", "invalid_course_code"),
        ],
    )
    def test_validate_invalid_attribute(
        self, function_name, function_args, request: pytest.FixtureRequest
    ):
        with pytest.raises(ValueError):
            if function_name == "validate_email_domain":
                args = request.getfixturevalue(function_args)
                if not isinstance(args, EmailStr):
                    raise ValueError
            func = globals()[function_name]
            func(request.getfixturevalue(function_args))

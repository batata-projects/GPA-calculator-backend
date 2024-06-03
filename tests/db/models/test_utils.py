import pytest


class TestUtils:
    @pytest.mark.parametrize(
        "function_name, function_args",
        [
            ("validate_uuid", "valid_uuid"),
            ("validate_email_str", "valid_email"),
            ("validate_term_str", "valid_term"),
            ("validate_course_name", "valid_course_name"),
            ("validate_course_code", "valid_course_code"),
        ],
    )
    def test_validate_successful(
        self,
        function_name,
        function_args,
        valid_uuid,
        valid_email,
        valid_term,
        valid_course_name,
        valid_course_code,
        request: pytest.FixtureRequest,
    ):
        func = globals()[function_name]
        assert func(request.getfixturevalue(function_args)) == request.getfixturevalue(
            function_args
        )

    @pytest.mark.parametrize(
        "function_name, function_args",
        [
            ("validate_uuid", "invalid_uuid"),
            ("validate_email_str", "invalid_email"),
            ("validate_email_str", "invalid_domain"),
            ("validate_term_str", "invalid_term"),
            ("validate_course_name", "invalid_course_name"),
            ("validate_course_code", "invalid_course_code"),
        ],
    )
    def test_validate_invalid(
        self,
        function_name,
        function_args,
        invalid_uuid,
        invalid_email,
        invalid_domain,
        invalid_term,
        invalid_course_name,
        invalid_course_code,
        request: pytest.FixtureRequest,
    ):
        with pytest.raises(ValueError):
            func = globals()[function_name]
            func(request.getfixturevalue(function_args))

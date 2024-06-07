import pytest

from src.common.utils.types.CourseCodeStr import validate_course_code  # noqa: F401
from src.common.utils.types.CourseNameStr import validate_course_name  # noqa: F401
from src.common.utils.types.TermStr import validate_term_str  # noqa: F401
from src.common.utils.types.UuidStr import validate_uuid  # noqa: F401


class TestUtils:
    @pytest.mark.parametrize(
        "function_name, function_args",
        [
            ("validate_uuid", "valid_uuid"),
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
            ("validate_term_str", "invalid_term"),
            ("validate_course_name", "invalid_course_name"),
            ("validate_course_code", "invalid_course_code"),
        ],
    )
    def test_validate_invalid_attribute(
        self, function_name, function_args, request: pytest.FixtureRequest
    ):
        with pytest.raises(ValueError):
            func = globals()[function_name]
            func(request.getfixturevalue(function_args))

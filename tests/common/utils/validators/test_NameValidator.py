import pytest

from src.common.utils.validators import validate_name


class TestNameValidator:
    def test_name_validator_successful(self, valid_name: str) -> None:
        assert validate_name(valid_name) == valid_name

    @pytest.mark.parametrize(
        "invalid_name",
        [
            "invalid_name1",
            "invalid_name2",
            "invalid_name3",
        ],
    )
    def test_name_validator_invalid(
        self, invalid_name: str, request: pytest.FixtureRequest
    ) -> None:
        invalid_name = request.getfixturevalue(invalid_name)
        with pytest.raises(ValueError):
            validate_name(invalid_name)

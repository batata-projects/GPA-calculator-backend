import pytest

from src.common.utils.validators import validate_name


class TestNameValidator:
    def test_name_validator_successful(self, valid_name: str) -> None:
        assert validate_name(valid_name) == valid_name

    def test_name_validator_invalid(self, invalid_name: None) -> None:
        with pytest.raises(AttributeError):
            validate_name(invalid_name)  # type: ignore

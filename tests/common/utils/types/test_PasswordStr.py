import pytest

from src.common.utils.types.PasswordStr import PasswordStr, validate_password_str


class TestPasswordStr:
    def test_password_str_successful(self, valid_password: PasswordStr) -> None:
        assert validate_password_str(valid_password) == valid_password

    def test_term_str_invalid(self, invalid_password: PasswordStr) -> None:
        with pytest.raises(ValueError):
            validate_password_str(invalid_password)

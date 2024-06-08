import pytest

from src.common.utils.types.UsernameStr import UsernameStr, validate_username_str


class TestUsernameStr:
    def test_username_str_successful(self, valid_username: UsernameStr) -> None:
        assert validate_username_str(valid_username) == valid_username

    @pytest.mark.parametrize(
        "invalid_username", ["invalid_username1", "invalid_username2"]
    )
    def test_username_str_invalid(self, invalid_username: UsernameStr) -> None:
        with pytest.raises(ValueError):
            validate_username_str(invalid_username)

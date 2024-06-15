import pytest
from pydantic import EmailStr

from src.common.utils.validators import validate_email


class TestEmailValidator:
    def test_email_validator_successful(self, valid_email: EmailStr) -> None:
        assert validate_email(valid_email) == valid_email

    def test_email_validator_invalid(self, invalid_email: EmailStr) -> None:
        with pytest.raises(ValueError):
            validate_email(invalid_email)

from unittest.mock import Mock

import pytest
from pydantic import EmailStr

from src.db.models import User


class TestUser:
    def test_user_successful(self, uuid_generator: Mock) -> None:
        user_id = uuid_generator()
        email = "rayan@mail.com"
        first_name = "Rayan"
        last_name = "Fakhreddine"

        user = User(
            id=user_id,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )

        assert user.id == user_id
        assert user.email == email
        assert user.first_name == first_name
        assert user.last_name == last_name

    def test_user_no_id(self) -> None:
        email = "rayan@mail.com"
        first_name = "Rayan"
        last_name = "Fakhreddine"

        user = User(
            email=email,
            first_name=first_name,
            last_name=last_name,
        )

        assert user.id is None
        assert user.email == email
        assert user.first_name == first_name
        assert user.last_name == last_name

    def test_user_invalid_id(self) -> None:
        user_id = "invalid"
        email = "rayan@mail.com"
        first_name = "Rayan"
        last_name = "Fakhreddine"

        with pytest.raises(ValueError):
            User(
                id=user_id,
                email=email,
                first_name=first_name,
                last_name=last_name,
            )

    @pytest.mark.parametrize(
        "email, first_name, last_name",
        [
            (None, "Rayan", "Fakhreddine"),
            ("rayan@mail.com", None, "Fakhreddine"),
            ("rayan@mail.com", "Rayan", None),
        ],
    )
    def test_user_none_attribute(
        self,
        email: EmailStr,
        first_name: str,
        last_name: str,
    ) -> None:
        with pytest.raises(ValueError):
            User(
                email=email,
                first_name=first_name,
                last_name=last_name,
            )

    @pytest.mark.parametrize(
        "email, first_name, last_name",
        [
            ("jaadshaker@mail", "Jad", "Shaker"),
            ("rayan@mail.com", 123, "Fakhreddine"),
            (
                "rayan@mail.com",
                "Rayan",
                123,
            ),
        ],
    )
    def test_user_invalid_attribute(
        self,
        email: EmailStr,
        first_name: str,
        last_name: str,
    ) -> None:
        with pytest.raises(ValueError):
            User(
                email=email,
                first_name=first_name,
                last_name=last_name,
            )

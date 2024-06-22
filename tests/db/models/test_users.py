from unittest.mock import Mock

import pytest
from pydantic import EmailStr, NonNegativeFloat, NonNegativeInt

from src.db.models import User


class TestUser:
    def test_user_successful(self, valid_uuid: Mock) -> None:
        user_id = valid_uuid
        email = "rmf40@mail.aub.edu"
        first_name = "Rayan"
        last_name = "Fakhreddine"
        credits = 0
        counted_credits = 0
        grade = 0.0

        user = User(
            id=user_id,
            email=email,
            first_name=first_name,
            last_name=last_name,
            credits=credits,
            counted_credits=counted_credits,
            grade=grade,
        )

        assert user.id == user_id
        assert user.email == email
        assert user.first_name == first_name
        assert user.last_name == last_name
        assert user.credits == credits
        assert user.counted_credits == counted_credits
        assert user.grade == grade

    def test_user_no_id(self) -> None:
        email = "rmf40@mail.aub.edu"
        first_name = "Rayan"
        last_name = "Fakhreddine"
        credits = 0
        counted_credits = 0
        grade = 0.0

        user = User(
            email=email,
            first_name=first_name,
            last_name=last_name,
            credits=credits,
            counted_credits=counted_credits,
            grade=grade,
        )

        assert user.id is None
        assert user.email == email
        assert user.first_name == first_name
        assert user.last_name == last_name
        assert user.credits == credits
        assert user.counted_credits == counted_credits
        assert user.grade == grade

    def test_user_invalid_id(self) -> None:
        user_id = "invalid"
        email = "rmf40@mail.aub.edu"
        first_name = "Rayan"
        last_name = "Fakhreddine"
        credits = 0
        counted_credits = 0
        grade = 0.0

        with pytest.raises(ValueError):
            User(
                id=user_id,
                email=email,
                first_name=first_name,
                last_name=last_name,
                credits=credits,
                counted_credits=counted_credits,
                grade=grade,
            )

    @pytest.mark.parametrize(
        "email, first_name, last_name, credits, counted_credits, grade",
        [
            (None, "Rayan", "Fakhreddine", 0, 0, 0.0),
            ("rmf40@mail.aub.edu", None, "Fakhreddine", 0, 0, 0.0),
            ("rmf40@mail.aub.edu", "Rayan", None, 0, 0, 0.0),
            ("rmf40@mail.aub.edu", "Rayan", "Fakhreddine", None, 0, 0.0),
            ("rmf40@mail.aub.edu", "Rayan", "Fakhreddine", 0, None, 0.0),
            ("rmf40@mail.aub.edu", "Rayan", "Fakhreddine", 0, 0, None),
        ],
    )
    def test_user_none_attribute(
        self,
        email: EmailStr,
        first_name: str,
        last_name: str,
        credits: NonNegativeInt,
        counted_credits: NonNegativeInt,
        grade: NonNegativeFloat,
    ) -> None:
        with pytest.raises(ValueError):
            User(
                email=email,
                first_name=first_name,
                last_name=last_name,
                credits=credits,
                counted_credits=counted_credits,
                grade=grade,
            )

    @pytest.mark.parametrize(
        "email, first_name, last_name, credits, counted_credits, grade",
        [
            ("jaadshaker@hotmail.com", "Jad", "Shaker", 0, 0, 0.0),
            ("rmf40@mail.aub.edu", 123, "Fakhreddine", 0, 0, 0.0),
            ("rmf40@mail.aub.edu", "Rayan", 123, 0, 0, 0.0),
            ("rmf40@mail.aub.edu", "Rayan", "Fakhreddine", -1, 0, 0.0),
            ("rmf40@mail.aub.edu", "Rayan", "Fakhreddine", 0, -1, 0.0),
            ("rmf40@mail.aub.edu", "Rayan", "Fakhreddine", 0, 0, -1),
        ],
    )
    def test_user_invalid_attribute(
        self,
        email: EmailStr,
        first_name: str,
        last_name: str,
        credits: NonNegativeInt,
        counted_credits: NonNegativeInt,
        grade: NonNegativeFloat,
    ) -> None:
        with pytest.raises(ValueError):
            User(
                email=email,
                first_name=first_name,
                last_name=last_name,
                credits=credits,
                counted_credits=counted_credits,
                grade=grade,
            )

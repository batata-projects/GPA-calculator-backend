from unittest.mock import Mock

import pytest

from src.db.models.users import User


class TestUser:
    def test_user_successful(self, uuid4: Mock):
        user_id = str(uuid4())
        email = "rmf40@mail.aub.edu"
        username = "Rio"
        first_name = "Rayan"
        last_name = "Fakhreddine"
        credits = 0
        counted_credits = 0
        grade = 0.0

        user = User(
            id=user_id,
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            credits=credits,
            counted_credits=counted_credits,
            grade=grade,
        )

        assert user.id == user_id
        assert user.email == email
        assert user.username == username
        assert user.first_name == first_name
        assert user.last_name == last_name
        assert user.credits == credits
        assert user.counted_credits == counted_credits
        assert user.grade == grade

    def test_user_no_id(self):
        email = "rmf40@mail.aub.edu"
        username = "Rio"
        first_name = "Rayan"
        last_name = "Fakhreddine"
        credits = 0
        counted_credits = 0
        grade = 0.0

        user = User(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            credits=credits,
            counted_credits=counted_credits,
            grade=grade,
        )

        assert user.id is None
        assert user.email == email
        assert user.username == username
        assert user.first_name == first_name
        assert user.last_name == last_name
        assert user.credits == credits
        assert user.counted_credits == counted_credits
        assert user.grade == grade

    @pytest.mark.parametrize(
        "email, username, first_name, last_name, credits, counted_credits, grade",
        [
            (None, "Rio", "Rayan", "Fakhreddine", 0, 0, 0.0),
            ("rmf40@mail.aub.edu", None, "Rayan", "Fakhreddine", 0, 0, 0.0),
            ("rmf40@mail.aub.edu", "Rio", None, "Fakhreddine", 0, 0, 0.0),
            ("rmf40@mail.aub.edu", "Rio", "Rayan", None, 0, 0, 0.0),
            ("rmf40@mail.aub.edu", "Rio", "Rayan", "Fakhreddine", None, 0, 0.0),
            ("rmf40@mail.aub.edu", "Rio", "Rayan", "Fakhreddine", 0, None, 0.0),
            ("rmf40@mail.aub.edu", "Rio", "Rayan", "Fakhreddine", 0, 0, None),
        ],
    )
    def test_user_none_attribute(
        self,
        email,
        username,
        first_name,
        last_name,
        credits,
        counted_credits,
        grade,
    ):
        with pytest.raises(ValueError):
            User(
                email=email,
                username=username,
                first_name=first_name,
                last_name=last_name,
                credits=credits,
                counted_credits=counted_credits,
                grade=grade,
            )

    @pytest.mark.parametrize(
        "email, username, first_name, last_name, credits, counted_credits, grade",
        [
            ("jaadshaker@gmail.com", "jss", "Jad", "Shaker", 0, 0, 0.0),
            ("rmf40@mail.aub.edu", "Invalid Username", "Rayan", "Fakhreddine", 0, 0, 0),
            ("rmf40@mail.aub.edu", "Rio", 123, "Fakhreddine", 0, 0, 0.0),
            ("rmf40@mail.aub.edu", "Rio", "Rayan", 123, 0, 0, 0.0),
            ("rmf40@mail.aub.edu", "Rio", "Rayan", "Fakhreddine", -1, 0, 0.0),
            ("rmf40@mail.aub.edu", "Rio", "Rayan", "Fakhreddine", 0, -1, 0.0),
            ("rmf40@mail.aub.edu", "Rio", "Rayan", "Fakhreddine", 0, 0, -1),
        ],
    )
    def test_user_invalid_attribute(
        self,
        email,
        username,
        first_name,
        last_name,
        credits,
        counted_credits,
        grade,
    ):
        with pytest.raises(ValueError):
            User(
                email=email,
                username=username,
                first_name=first_name,
                last_name=last_name,
                credits=credits,
                counted_credits=counted_credits,
                grade=grade,
            )

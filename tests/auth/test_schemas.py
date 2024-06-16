import pytest

from src.auth.schemas import LoginRequest, RegisterRequest


class TestRegisterRequest:
    def test_register_request_successful(self) -> None:
        register_request = RegisterRequest(
            first_name="First",
            last_name="Last",
            email="username@mail.aub.edu",
            username="username",
            password="Password123",
        )
        assert register_request.first_name == "First"
        assert register_request.last_name == "Last"
        assert register_request.email == "username@mail.aub.edu"
        assert register_request.username == "username"
        assert register_request.password == "Password123"
        assert register_request.auth_model_dump() == {
            "email": "username@mail.aub.edu",
            "password": "Password123",
            "options": {
                "data": {
                    "username": "username",
                    "first_name": "First",
                    "last_name": "Last",
                }
            },
        }

    def test_register_request_default(self) -> None:
        register_request = RegisterRequest()
        assert register_request.first_name == "First Name"
        assert register_request.last_name == "Last Name"
        assert register_request.email == "username@mail.aub.edu"
        assert register_request.username == "username"
        assert register_request.password == "Password123"
        assert register_request.auth_model_dump() == {
            "email": "username@mail.aub.edu",
            "password": "Password123",
            "options": {
                "data": {
                    "username": "username",
                    "first_name": "First Name",
                    "last_name": "Last Name",
                }
            },
        }

    @pytest.mark.parametrize(
        "first_name, last_name, email, username, password",
        [
            (12345, "Last", "username@mail.aub.edu", "username", "Password123"),
            ("First", 12345, "username@mail.aub.edu", "username", "Password123"),
            ("First", "Last", "username@hotmail.com", "username", "Password123"),
            (
                "First",
                "Last",
                "username@mail.aub.edu",
                "invalid username",
                "Password123",
            ),
            ("First", "Last", "username@mail.aub.edu", "username", "password123"),
        ],
    )
    def test_register_request_invalid(
        self, first_name: str, last_name: str, email: str, username: str, password: str
    ) -> None:
        with pytest.raises(ValueError):
            RegisterRequest(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password,
            )


class TestLoginRequest:
    def test_login_request_successful(self) -> None:
        login_request = LoginRequest(
            email="username@mail.aub.edu", password="Password123"
        )
        assert login_request.email == "username@mail.aub.edu"
        assert login_request.password == "Password123"
        assert login_request.auth_model_dump() == {
            "email": "username@mail.aub.edu",
            "password": "Password123",
        }

    def test_login_request_default(self) -> None:
        login_request = LoginRequest()
        assert login_request.email == "username@mail.aub.edu"
        assert login_request.password == "Password123"
        assert login_request.auth_model_dump() == {
            "email": "username@mail.aub.edu",
            "password": "Password123",
        }

    @pytest.mark.parametrize(
        "email, password",
        [
            ("username@hotmail.com", "Password123"),
            ("username@mail.aub.edu", "password123"),
        ],
    )
    def test_login_request_invalid(self, email: str, password: str) -> None:
        with pytest.raises(ValueError):
            LoginRequest(email=email, password=password)

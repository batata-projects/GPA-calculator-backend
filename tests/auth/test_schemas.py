import pytest

from src.auth.schemas import LoginRequest, RegisterRequest


class TestRegisterRequest:
    def test_register_request_successful(self) -> None:
        register_request = RegisterRequest(
            first_name="First",
            last_name="Last",
            email="email@mail.aub.edu",
            password="Password123",
        )
        assert register_request.first_name == "First"
        assert register_request.last_name == "Last"
        assert register_request.email == "email@mail.aub.edu"
        assert register_request.password == "Password123"
        assert register_request.auth_model_dump() == {
            "email": "email@mail.aub.edu",
            "password": "Password123",
            "options": {
                "data": {
                    "first_name": "First",
                    "last_name": "Last",
                }
            },
        }

    def test_register_request_default(self) -> None:
        register_request = RegisterRequest()
        assert register_request.first_name == "First Name"
        assert register_request.last_name == "Last Name"
        assert register_request.email == "email@mail.aub.edu"
        assert register_request.password == "Password123"
        assert register_request.auth_model_dump() == {
            "email": "email@mail.aub.edu",
            "password": "Password123",
            "options": {
                "data": {
                    "first_name": "First Name",
                    "last_name": "Last Name",
                }
            },
        }

    @pytest.mark.parametrize(
        "first_name, last_name, email, password",
        [
            (12345, "Last", "email@mail.aub.edu", "Password123"),
            ("First", 12345, "email@mail.aub.edu", "Password123"),
            ("First", "Last", "email@hotmail", "Password123"),
            ("First", "Last", "email@mail.aub.edu", "password123"),
        ],
    )
    def test_register_request_invalid(
        self, first_name: str, last_name: str, email: str, password: str
    ) -> None:
        with pytest.raises(ValueError):
            RegisterRequest(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
            )


class TestLoginRequest:
    def test_login_request_successful(self) -> None:
        login_request = LoginRequest(email="email@mail.aub.edu", password="Password123")
        assert login_request.email == "email@mail.aub.edu"
        assert login_request.password == "Password123"

    def test_login_request_default(self) -> None:
        login_request = LoginRequest()
        assert login_request.email == "email@mail.aub.edu"
        assert login_request.password == "Password123"

    @pytest.mark.parametrize(
        "email, password",
        [
            ("email@hotmail", "Password123"),
            ("email@mail.aub.edu", "password123"),
        ],
    )
    def test_login_request_invalid(self, email: str, password: str) -> None:
        with pytest.raises(ValueError):
            LoginRequest(email=email, password=password)

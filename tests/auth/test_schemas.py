import pytest

from src.auth.schemas import LoginRequest, RegisterRequest, ResetPasswordRequest


class TestRegisterRequest:
    def test_register_request_successful(self) -> None:
        register_request = RegisterRequest(
            first_name="First",
            last_name="Last",
            email="email@mail.com",
            password="Password123",
        )
        assert register_request.first_name == "First"
        assert register_request.last_name == "Last"
        assert register_request.email == "email@mail.com"
        assert register_request.password == "Password123"
        assert register_request.auth_model_dump() == {
            "email": "email@mail.com",
            "password": "Password123",
            "options": {
                "data": {
                    "first_name": "First",
                    "last_name": "Last",
                }
            },
        }

    @pytest.mark.parametrize(
        "first_name, last_name, email, password",
        [
            (12345, "Last", "email@mail.com", "Password123"),
            ("First", 12345, "email@mail.com", "Password123"),
            ("First", "Last", "email@mail", "Password123"),
            ("First", "Last", "email@mail.com", "password123"),
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
        login_request = LoginRequest(email="email@mail.com", password="Password123")
        assert login_request.email == "email@mail.com"
        assert login_request.password == "Password123"
        assert login_request.auth_model_dump() == {
            "email": "email@mail.com",
            "password": "Password123",
        }

    @pytest.mark.parametrize(
        "email, password",
        [
            ("email@mail", "Password123"),
            ("email@mail.com", "password123"),
        ],
    )
    def test_login_request_invalid(self, email: str, password: str) -> None:
        with pytest.raises(ValueError):
            LoginRequest(email=email, password=password)


class TestForgetPasswordRequest:
    def test_forget_password_request_successful(self) -> None: ...

    def test_forget_password_request_invalid(self) -> None: ...


class TestResetPasswordRequest:
    def test_reset_password_request_successful(self) -> None:
        password_reset_request = ResetPasswordRequest(password="Password123")
        assert password_reset_request.password == "Password123"
        assert password_reset_request.model_dump() == {
            "password": "Password123",
        }

    @pytest.mark.parametrize("password", ["password123"])
    def test_reset_password_request_invalid(self, password: str) -> None:
        with pytest.raises(ValueError):
            ResetPasswordRequest(password=password)


class TestOTPRequest:
    def test_otp_request_successful(self) -> None: ...

    def test_otp_request_invalid(self) -> None: ...


class TestSignInWithOTPRequest:
    def test_sign_in_with_otp_request_successful(self) -> None: ...

    def test_sign_in_with_otp_request_invalid(self) -> None: ...

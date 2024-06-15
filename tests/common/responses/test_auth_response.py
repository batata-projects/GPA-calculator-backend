import pytest

from src.common.responses import AuthResponse
from src.common.session import Session
from src.db.models import User


class TestAuthResponse:
    def test_auth_response_successful(self, user1: User, session: Session) -> None:
        response = AuthResponse(user=user1, session=session)
        assert response.user == user1
        assert response.session == session
        assert response.model_dump() == {
            "user": user1.model_dump(),
            "session": session.model_dump(),
        }

    def test_auth_response_invalid_user(self, session: Session) -> None:
        with pytest.raises(ValueError):
            AuthResponse(user={"name": "joe"}, session=session)  # type:ignore

    def test_auth_response_invalid_session(self, user1: User) -> None:
        with pytest.raises(ValueError):
            AuthResponse(user=user1, session={"token": "invalid_token"})  # type:ignore

import pytest
from gotrue.types import Session as GoTrueSession  # type: ignore

from src.common.session import Session


class TestSession:
    def test_session_successful(self) -> None:
        session = Session(
            access_token="access token", refresh_token="refresh token", expires_in=3600
        )
        assert session.access_token == "access token"
        assert session.refresh_token == "refresh token"
        assert session.expires_in == 3600
        assert session.model_dump() == {
            "access_token": "access token",
            "refresh_token": "refresh token",
            "expires_in": 3600,
        }

    def test_session_invalid(self) -> None:
        with pytest.raises(ValueError):
            Session(
                access_token="access token",
                refresh_token="refresh token",
                expires_in=-1,
            )

    @pytest.mark.parametrize(
        "access_token, refresh_token, expires_in",
        [
            (None, "refresh token", 3600),
            ("access token", None, 3600),
            ("access token", "refresh token", None),
        ],
    )
    def test_session_invalid_none(
        self,
        access_token: str,
        refresh_token: str,
        expires_in: int,
    ) -> None:
        with pytest.raises(ValueError):
            Session(
                access_token=access_token,
                refresh_token=refresh_token,
                expires_in=expires_in,
            )

    def test_validate_supabase_session_successful(
        self, gotrue_session: GoTrueSession
    ) -> None:
        session = Session.validate_supabase_session(gotrue_session)
        assert session.access_token == gotrue_session.access_token
        assert session.refresh_token == gotrue_session.refresh_token
        assert session.expires_in == gotrue_session.expires_in
        assert session.model_dump() == {
            "access_token": gotrue_session.access_token,
            "refresh_token": gotrue_session.refresh_token,
            "expires_in": gotrue_session.expires_in,
        }

    def test_validate_supabase_session_invalid(
        self, gotrue_session: GoTrueSession
    ) -> None:
        gotrue_session.expires_in = -1
        with pytest.raises(ValueError):
            Session.validate_supabase_session(gotrue_session)

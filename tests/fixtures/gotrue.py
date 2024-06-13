import pytest
from gotrue.types import Session as GoTrueSession  # type: ignore
from gotrue.types import User as GoTrueUser

from src.common.responses import Session
from src.db.models.users import User


@pytest.fixture
def gotrue_user(user1: User) -> GoTrueUser:
    return GoTrueUser(
        id=user1.id,
        email=user1.email,
        user_metadata={
            "username": user1.username,
            "first_name": user1.first_name,
            "last_name": user1.last_name,
            "credits": user1.credits,
            "counted_credits": user1.counted_credits,
            "grade": user1.grade,
        },
        aud="authenticated",
        app_metadata={},
        created_at="2021-10-10T10:10:10.000Z",
    )


@pytest.fixture
def gotrue_session(session: Session, gotrue_user: GoTrueUser) -> GoTrueSession:
    return GoTrueSession(
        access_token=session.access_token,
        refresh_token=session.refresh_token,
        expires_in=session.expires_in,
        token_type="Bearer",
        user=gotrue_user,
    )

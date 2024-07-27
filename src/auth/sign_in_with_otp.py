from src.auth.schemas import SignInWithOTPRequest
from src.common.responses import AuthResponse
from src.common.session import Session
from src.db.dao import UserDAO
from src.db.models import User


def sign_in_with_otp(request: SignInWithOTPRequest, user_dao: UserDAO) -> AuthResponse:
    response = user_dao.client.auth.verify_otp(
        {"email": request.email, "token": request.otp, "type": "recovery"}
    )
    user = User.validate_supabase_user(response.user)
    session = Session.validate_supabase_session(response.session)
    return AuthResponse(user=user, session=session)

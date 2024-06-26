# implement reset password and forgot password using supabase API


from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema
from pydantic import EmailStr
from supabase import create_client

from src.config import Config

router = APIRouter()

# Supabase credentials
SUPABASE_URL = Config.SUPABASE.URL
SUPABASE_KEY = Config.SUPABASE.KEY
assert SUPABASE_URL is not None
assert SUPABASE_KEY is not None
supabase_client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Email credentials
conf = ConnectionConfig(
    MAIL_USERNAME="username",
    MAIL_PASSWORD="**********",
    MAIL_FROM="test@email.com",
    MAIL_PORT=465,
    MAIL_SERVER="mail server",
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=True,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
)


@router.post("/forgot_password")
async def forgot_password(email: EmailStr) -> JSONResponse:
    # check if email exists in the database
    user = await supabase_client.auth.get_user_by_email(email)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # generate a token
    token = await supabase_client.auth.api.create_password_reset_token(email)

    # send email
    message = MessageSchema(
        subject="Reset Password",
        recipients=[email],
        body=f"Click this link to reset your password: http://localhost:3000/reset_password?token={token['access_token']}",
        subtype="html",
    )
    fm = FastMail(conf)
    await fm.send_message(message)

    return JSONResponse(content={"message": "Email sent"})

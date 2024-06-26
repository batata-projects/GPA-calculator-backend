# implement reset password and forgot password using supabase API

from supabase import create_client
from supabase.client import Client
import os
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig 
from pydantic import EmailStr
from typing import Optional
from config import Config
router = APIRouter()

# Supabase credentials
SUPABASE_URL = Config.SUPABASE.URL
SUPABASE_KEY = Config.SUPABASE.KEY
supabase_client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Email credentials
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
conf = ConnectionConfig(
    MAIL_USERNAME=EMAIL,
    MAIL_PASSWORD=PASSWORD,
    MAIL_FROM=EMAIL,
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_TLS=True,
    MAIL_SSL=False,
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
    )
    fm = FastMail(conf)
    await fm.send_message(message)

    return JSONResponse(content={"message": "Email sent"})


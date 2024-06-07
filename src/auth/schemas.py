from typing import Optional

from pydantic import BaseModel, EmailStr, field_validator

from src.common.utils.types.PasswordStr import PasswordStr
from src.common.utils.types.UsernameStr import UsernameStr


class RegisterRequest(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: Optional[UsernameStr] = None
    email: Optional[EmailStr] = None
    password: PasswordStr

    @field_validator("first_name", "last_name")
    def name_validator(cls, v: str) -> str:
        if v:
            return v.title()
        return v

    @field_validator("email")
    def validate_email_domain(cls, v: EmailStr) -> EmailStr:
        try:
            domain = v.split("@")[1]
            if domain not in ["aub.edu.lb", "mail.aub.edu"]:
                raise ValueError
        except ValueError:
            raise ValueError(f"{v} is an invalid email")
        return v

    def auth_model_dump(self):
        return {
            "email": self.email,
            "password": self.password,
            "options": {
                "data": {
                    "username": self.username,
                    "first_name": self.first_name,
                    "last_name": self.last_name,
                }
            },
        }


class LoginRequest(BaseModel):
    email: EmailStr
    password: PasswordStr

    @field_validator("email")
    def validate_email_domain(cls, v: EmailStr) -> EmailStr:
        try:
            domain = v.split("@")[1]
            if domain not in ["aub.edu.lb", "mail.aub.edu"]:
                raise ValueError
        except ValueError:
            raise ValueError(f"{v} is an invalid email")
        return v

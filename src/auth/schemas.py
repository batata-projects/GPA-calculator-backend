from typing import Optional, Union

from pydantic import BaseModel, EmailStr, Field, field_validator

from src.common.utils.types.PasswordStr import PasswordStr
from src.common.utils.types.UsernameStr import UsernameStr


class RegisterRequest(BaseModel):
    first_name: Optional[str] = Field(default="First Name", description="First Name")
    last_name: Optional[str] = Field(default="Last Name", description="Last Name")
    email: EmailStr = Field(
        default="username@mail.aub.edu", description="Email must be an AUB email"
    )
    username: Optional[UsernameStr] = Field(default="username", description="Username")
    password: PasswordStr = Field(
        default="Password123",
        description="Password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, and one number.",
    )

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

    def auth_model_dump(
        self,
    ) -> dict[str, Union[str, dict[str, dict[str, Optional[str]]]]]:
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
    email: EmailStr = Field(
        default="username@mail.aub.edu", description="Email must be an AUB email"
    )
    password: PasswordStr = Field(
        default="Password123",
        description="Password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, and one number.",
    )

    @field_validator("email")
    def validate_email_domain(cls, v: EmailStr) -> EmailStr:
        try:
            domain = v.split("@")[1]
            if domain not in ["aub.edu.lb", "mail.aub.edu"]:
                raise ValueError
        except ValueError:
            raise ValueError(f"{v} is an invalid email")
        return v

    def auth_model_dump(self) -> dict[str, str]:
        return {
            "email": self.email,
            "password": self.password,
        }

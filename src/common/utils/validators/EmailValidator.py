from pydantic import EmailStr


def validate_email(v: EmailStr) -> EmailStr:
    try:
        domain = v.split("@")[1]
        if domain not in ["aub.edu.lb", "mail.aub.edu", "gmail.com"]:
            raise ValueError
    except ValueError:
        raise ValueError(f"{v} is an invalid email")
    return v

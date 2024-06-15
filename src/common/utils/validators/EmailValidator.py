from pydantic import EmailStr


def validate_email_domain(v: EmailStr) -> EmailStr:
    return v
    try:
        domain = v.split("@")[1]
        if domain not in ["aub.edu.lb", "mail.aub.edu"]:
            raise ValueError
    except ValueError:
        raise ValueError(f"{v} is an invalid email")
    return v

from typing import Annotated, Optional

from pydantic.functional_validators import BeforeValidator


def validate_username_str(v: Optional[str] = None) -> Optional[str]:
    if not v:
        return None
    try:
        if not v.isalnum() or " " in v:
            raise ValueError
        return v
    except ValueError:
        raise ValueError(f"{v} is an invalid username")


UsernameStr = Annotated[str, BeforeValidator(validate_username_str)]

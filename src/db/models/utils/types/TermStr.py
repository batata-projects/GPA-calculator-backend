from typing import Annotated, Optional

from pydantic.functional_validators import BeforeValidator


def validate_term_str(v: Optional[str] = None) -> Optional[str]:
    if not v:
        return None
    try:
        term_name, start, _, end = v.split()
        if term_name not in ["Fall", "Spring", "Summer", "Winter"]:
            raise ValueError
        if not 2010 <= int(start) + 1 == int(end) <= 2100:
            raise ValueError
        if not _ == "-":
            raise ValueError
        return v
    except ValueError:
        raise ValueError(f"{v} is an invalid term string")


TermStr = Annotated[str, BeforeValidator(validate_term_str)]

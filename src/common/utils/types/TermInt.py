from typing import Annotated

from pydantic.functional_validators import BeforeValidator


def validate_term_int(v: int) -> int:
    if not v:
        raise ValueError("Term cannot be empty")
    year = v // 100
    if not 1000 <= year <= 9999:
        raise ValueError(f"Invalid year: {year}")
    return v


TermInt = Annotated[int, BeforeValidator(validate_term_int)]

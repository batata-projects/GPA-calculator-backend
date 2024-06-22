from typing import Annotated

from pydantic.functional_validators import BeforeValidator


def validate_term_int(v: int) -> int:
    year = v // 100
    if not 1000 <= year <= 9999:
        raise ValueError(f"Invalid year: {year}")
    return v


TermInt = Annotated[int, BeforeValidator(validate_term_int)]

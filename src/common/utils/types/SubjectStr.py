from typing import Annotated

from pydantic.functional_validators import BeforeValidator


# TODO: Add tests
def validate_subject_str(v: str) -> str:
    if not v:
        raise ValueError("Subject cannot be empty")
    if not v.isupper():
        raise ValueError("Subject must be in uppercase")
    return v


SubjectStr = Annotated[str, BeforeValidator(validate_subject_str)]

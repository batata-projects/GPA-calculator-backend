from typing import Annotated

from pydantic.functional_validators import BeforeValidator


def validate_subject_str(v: str) -> str:
    if not v:
        raise ValueError("Subject cannot be empty")
    return v.upper()


SubjectStr = Annotated[str, BeforeValidator(validate_subject_str)]

import uuid
from typing import Annotated, Optional

from pydantic.functional_validators import BeforeValidator


def validate_uuid(v: Optional[str] = None) -> Optional[str]:
    if not v:
        return None
    try:
        uuid.UUID(v)
    except ValueError:
        raise ValueError(f"{v} is an invalid UUID")
    return v


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


def validate_username_str(v: Optional[str] = None) -> Optional[str]:
    if not v:
        return None
    try:
        if not v.isalnum():
            raise ValueError
        return v
    except ValueError:
        raise ValueError(f"{v} is an invalid username")


def validate_course_name(v: Optional[str] = None) -> Optional[str]:
    if not v:
        return None
    try:
        if len(v) != 4 or not v.isalpha():
            raise ValueError
        return v
    except ValueError:
        raise ValueError(f"{v} is an invalid course name")


def validate_course_code(v: Optional[str] = None) -> Optional[str]:
    if not v:
        return None
    try:
        if len(v) < 3 or len(v) > 5 or not v.isalnum() or v[0].isalpha():
            raise ValueError
        return v
    except ValueError:
        raise ValueError(f"{v} is an invalid course code")


def validate_non_negative_int(v: Optional[int] = None) -> Optional[int]:
    if not v:
        return None
    if v < 0:
        raise ValueError(f"{v} is a negative integer")
    return v


def validate_non_negative_float(v: Optional[float] = None) -> Optional[float]:
    if not v:
        return None
    if v < 0:
        raise ValueError(f"{v} is a negative float")
    return v


def validate_bool(v: Optional[bool] = None) -> Optional[bool]:
    if not v:
        return None
    if not isinstance(v, bool):
        raise ValueError(f"{v} is not a boolean")
    return v


UuidStr = Annotated[str, BeforeValidator(validate_uuid)]
TermStr = Annotated[str, BeforeValidator(validate_term_str)]
UsernameStr = Annotated[str, BeforeValidator(validate_username_str)]
CourseNameStr = Annotated[str, BeforeValidator(validate_course_name)]
CourseCodeStr = Annotated[str, BeforeValidator(validate_course_code)]

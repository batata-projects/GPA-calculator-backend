def validate_name(v: str) -> str:
    if v:
        return v.title()
    return v

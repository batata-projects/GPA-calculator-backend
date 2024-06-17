from src.controller.schemas.users import UserQuery


def test_user_query() -> None:
    query = UserQuery()
    assert query is not None
    assert query.model_dump() == {
        "email": None,
        "username": None,
        "first_name": None,
        "last_name": None,
        "credits": None,
        "counted_credits": None,
        "grade": None,
    }

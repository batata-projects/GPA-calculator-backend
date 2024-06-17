from src.controller.routers.users import users_router


def test_users_router() -> None:
    assert users_router.prefix == "/users"
    assert users_router.tags == ["Users"]

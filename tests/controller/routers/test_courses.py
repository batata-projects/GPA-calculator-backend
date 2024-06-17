from src.controller.routers.courses import courses_router


def test_courses_router() -> None:
    assert courses_router.prefix == "/courses"
    assert courses_router.tags == ["Courses"]

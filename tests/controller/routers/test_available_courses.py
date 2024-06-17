from src.controller.routers.available_courses import available_courses_router


def test_available_courses_router() -> None:
    assert available_courses_router.prefix == "/available-courses"
    assert available_courses_router.tags == ["Available Courses"]

from src.controller.schemas.courses import CourseQuery


def test_course_query() -> None:
    query = CourseQuery()
    assert query is not None
    assert query.model_dump() == {
        "available_course_id": None,
        "user_id": None,
        "grade": None,
        "passed": None,
    }

from src.controller.schemas.courses import CourseQuery


def test_course_query() -> None:
    query = CourseQuery()
    assert query is not None
    assert query.model_dump() == {
        "user_id": None,
        "subject": None,
        "course_code": None,
        "term": None,
        "credits": None,
        "grade": None,
        "graded": None,
    }

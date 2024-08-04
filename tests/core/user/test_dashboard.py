from src.core.user.dashboard import Term, get_dashboard_data
from src.db.models import Course, User


class TestTerm:
    def test_term(self) -> None:
        term = Term(name="name")

        assert term.model_dump() == {
            "name": "name",
            "credits": 0,
            "counted_credits": 0,
            "grade": 0.0,
            "gpa": 0.0,
            "courses": {},
        }

    def test_term_with_values(self, course1: Course) -> None:
        assert course1.id is not None

        term = Term(
            name="name",
            credits=1,
            counted_credits=2,
            grade=3.0,
            gpa=4.0,
            courses={course1.id: course1},
        )

        assert term.model_dump() == {
            "name": "name",
            "credits": 1,
            "counted_credits": 2,
            "grade": 3.0,
            "gpa": 4.0,
            "courses": {course1.id: course1.model_dump()},
        }


class TestGetDashboardData:
    def test_get_dashboard_data(self, user1: User, courses: list[Course]) -> None:
        data = get_dashboard_data(user1, courses)

        assert data == {
            "user": {
                "id": user1.id,
                "email": "jad@mail.com",
                "first_name": "Jad",
                "last_name": "Shaker",
                "gpa": 4.3,
            },
            "terms": {
                202310: {
                    "name": "Fall 2023",
                    "gpa": 4.3,
                    "credits": 6,
                    "courses": {
                        courses[i].id: courses[i].model_dump(exclude={"id", "user_id"})
                        for i in range(len(courses))
                    },
                }
            },
        }

from src.db.tables import SupabaseTables


class TestSupabaseTables:
    def test_str(self) -> None:
        assert str(SupabaseTables.AVAILABLE_COURSES) == "available_courses"
        assert str(SupabaseTables.COURSES) == "courses"
        assert str(SupabaseTables.TERMS) == "terms"
        assert str(SupabaseTables.USERS) == "users"

from src.db.tables import SupabaseTables


class TestSupabaseTables:
    def test_str(self) -> None:
        assert SupabaseTables.AVAILABLE_COURSES == "available_courses"
        assert SupabaseTables.COURSES == "courses"
        assert SupabaseTables.TERMS == "terms"
        assert SupabaseTables.USERS == "users"

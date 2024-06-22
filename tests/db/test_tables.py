from src.db.tables import SupabaseTables


class TestSupabaseTables:
    def test_str(self) -> None:
        assert SupabaseTables.COURSES == "courses"
        assert SupabaseTables.USERS == "users"

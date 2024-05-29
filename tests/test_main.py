from src.main import app


class TestMain:
    def test_main_successful(self):
        assert app.title == "GPA Calculator"
        assert app.description == "A simple GPA calculator API"
        assert app.version == "0.1.0"

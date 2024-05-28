from src.main import app


def test_main():
    assert app.title == "GPA Calculator"
    assert app.description == "A simple GPA calculator API"
    assert app.version == "0.1.0"
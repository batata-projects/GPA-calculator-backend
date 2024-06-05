from src.config import Config


class TestConfig:
    def test_config(self):
        assert Config.APP.TITLE == "GPA Calculator"
        assert Config.APP.DESCRIPTION == "A simple GPA calculator API"
        assert Config.APP.VERSION == "0.1.0"
        assert Config.Testing.RANDOM.SEED == 0

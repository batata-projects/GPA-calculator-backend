from src.config import config
from src.main import app


class TestMain:
    def test_main_successful(self):
        assert app.title == config.APP.TITLE
        assert app.description == config.APP.DESCRIPTION
        assert app.version == config.APP.VERSION

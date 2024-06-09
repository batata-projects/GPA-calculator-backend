from unittest.mock import patch
import pytest

from src.config import Config


@pytest.fixture
def mock_config():
    with patch.object(Config.SUPABASE, 'KEY', 'mock_key'), \
         patch.object(Config.SUPABASE, 'URL', 'http://mock_url'):
        yield

@pytest.fixture
def mock_access_token():
    with patch("src.auth.dependencies.get_access_token") as mock_access_token:
        yield mock_access_token

@pytest.fixture
def mock_refresh_token():
    with patch("src.auth.dependencies.get_refresh_token") as mock_refresh_token:
        yield mock_refresh_token

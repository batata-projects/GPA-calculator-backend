import pytest
from unittest.mock import patch
from src.config import Config
from unittest.mock import patch, Mock
from supabase import Client

# Mock Config for tests
@pytest.fixture
def mock_config():
    with patch.object(Config.SUPABASE, 'KEY', 'mock_key'), \
         patch.object(Config.SUPABASE, 'URL', 'http://mock_url'):
        yield

# Mock the Supabase client creation
@pytest.fixture
def mock_authenticated_client(mocker):
    mock_client = Mock(spec=Client)
    mocker.patch("src.db.base.get_authenticated_client", return_value=mock_client)
    return mock_client

@pytest.fixture
def mock_unauthenticated_client(mocker):
    mock_client = Mock(spec=Client)
    mocker.patch("src.db.base.get_unauthenticated_client", return_value=mock_client)
    return mock_client
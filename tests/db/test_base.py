from fastapi.security import HTTPAuthorizationCredentials
import pytest
from unittest.mock import Mock
from supabase import Client
from src.auth.dependencies import get_access_token, get_refresh_token
from src.config import Config
from src.db.base import get_authenticated_client, get_unauthenticated_client

@pytest.mark.asyncio
class TestGetClient:
    async def test_get_authenticated_client_success(mock_config, mocker, mock_access_token, mock_refresh_token):
        # mocker.patch("src.auth.dependencies.get_access_token", return_value=mock_access_token)
        # mocker.patch("src.auth.dependencies.get_refresh_token", return_value=mock_refresh_token)
        
        # mock_create_client = mocker.patch("supabase.create_client", autospec=True)
        # mock_client = Mock(spec=Client)
        # mock_create_client.return_value = mock_client

        # bearer = Mock(spec=HTTPAuthorizationCredentials)
        # access_token = await get_access_token(bearer=bearer)
        # refresh_token = await get_refresh_token(bearer=bearer)

        # client = get_authenticated_client(access_token=access_token, refresh_token=refresh_token)
        
        # mock_create_client.assert_called_once_with(
        #     supabase_url=Config.SUPABASE.URL,
        #     supabase_key=Config.SUPABASE.KEY,
        # )
        # mock_client.auth.set_session.assert_called_once_with(
        #     access_token=mock_access_token,
        #     refresh_token=mock_refresh_token,
        # )
        # assert client == mock_client

        # Mock the access token and refresh token dependencies
        mock_access_token = "mock_access_token"
        mock_refresh_token = "mock_refresh_token"
        mocker.patch("src.auth.dependencies.get_access_token", return_value=mock_access_token)
        mocker.patch("src.auth.dependencies.get_refresh_token", return_value=mock_refresh_token)
        
        # Mock the Supabase client creation
        mock_create_client = mocker.patch("supabase.create_client", autospec=True)
        mock_client = Mock(spec=Client)
        mock_create_client.return_value = mock_client
        
        bearer = Mock(spec=HTTPAuthorizationCredentials)
        access_token = await get_access_token(bearer=bearer)
        refresh_token = await get_refresh_token(bearer=bearer)
        client = get_authenticated_client(access_token, refresh_token)
        
        # Verify the client creation and session setting
        mock_create_client.assert_called_once_with(
            supabase_url=Config.SUPABASE.URL,
            supabase_key=Config.SUPABASE.KEY,
        )
        mock_client.auth.set_session.assert_called_once_with(
            access_token=mock_access_token,
            refresh_token=mock_refresh_token,
        )
        assert client == mock_client

    def test_get_authenticated_client_missing_key(mocker):
        mocker.patch.object(Config.SUPABASE, 'KEY', None)
        mocker.patch.object(Config.SUPABASE, 'URL', 'http://mock_url')
        
        with pytest.raises(ValueError, match="SUPABASE_KEY and SUPABASE_URL must be set in the environment"):
            get_authenticated_client()

    def test_get_authenticated_client_missing_url(mocker):
        mocker.patch.object(Config.SUPABASE, 'KEY', 'mock_key')
        mocker.patch.object(Config.SUPABASE, 'URL', None)
        
        with pytest.raises(ValueError, match="SUPABASE_KEY and SUPABASE_URL must be set in the environment"):
            get_authenticated_client()

    def test_get_unauthenticated_client_success(mock_config, mocker):
        mock_create_client = mocker.patch("supabase.create_client", autospec=True)
        mock_client = Mock()
        mock_create_client.return_value = mock_client
        
        client = get_unauthenticated_client()
        
        mock_create_client.assert_called_once_with(
            supabase_url=Config.SUPABASE.URL,
            supabase_key=Config.SUPABASE.KEY,
        )
        assert client == mock_client

    def test_get_unauthenticated_client_missing_key(mocker):
        mocker.patch.object(Config.SUPABASE, 'KEY', None)
        mocker.patch.object(Config.SUPABASE, 'URL', 'http://mock_url')
        
        with pytest.raises(ValueError, match="SUPABASE_KEY and SUPABASE_URL must be set in the environment"):
            get_unauthenticated_client()

    def test_get_unauthenticated_client_missing_url(mocker):
        mocker.patch.object(Config.SUPABASE, 'KEY', 'mock_key')
        mocker.patch.object(Config.SUPABASE, 'URL', None)
        
        with pytest.raises(ValueError, match="SUPABASE_KEY and SUPABASE_URL must be set in the environment"):
            get_unauthenticated_client()

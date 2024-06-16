from unittest.mock import Mock, patch

import pytest

from src.db.base import get_authenticated_client, get_unauthenticated_client


@patch("src.db.base.Config")
@patch("src.db.base.create_client")
class TestGetAuthenticatedClient:
    def test_get_authenticated_client_success(
        self,
        mock_create_client: Mock,
        mock_config: Mock,
        valid_access_token: str,
        valid_refresh_token: str,
    ) -> None:
        mock_config.SUPABASE.KEY = "SUPABASE_KEY"
        mock_config.SUPABASE.URL = "SUPABASE_URL"
        mock_create_client.return_value = mock_client = Mock()
        mock_client.auth.set_session.return_value = None

        client = get_authenticated_client(
            access_token=valid_access_token, refresh_token=valid_refresh_token
        )

        assert client == mock_client
        mock_create_client.assert_called_once_with(
            supabase_url="SUPABASE_URL", supabase_key="SUPABASE_KEY"
        )

    def test_get_authenticated_client_missing_key(
        self,
        mock_create_client: Mock,
        mock_config: Mock,
        valid_access_token: str,
        valid_refresh_token: str,
    ) -> None:
        mock_config.SUPABASE.KEY = None
        mock_config.SUPABASE.URL = "SUPABASE_URL"

        with pytest.raises(
            ValueError,
            match="SUPABASE_KEY and SUPABASE_URL must be set in the environment",
        ):
            get_authenticated_client(
                access_token=valid_access_token, refresh_token=valid_refresh_token
            )


@patch("src.db.base.Config")
@patch("src.db.base.create_client")
class TestGetUnauthenticatedClient:
    def test_get_unauthenticated_client_success(
        self, mock_create_client: Mock, mock_config: Mock
    ) -> None:
        mock_config.SUPABASE.KEY = "SUPABASE_KEY"
        mock_config.SUPABASE.URL = "SUPABASE_URL"
        mock_create_client.return_value = mock_client = Mock()

        client = get_unauthenticated_client()

        assert client == mock_client
        mock_create_client.assert_called_once_with(
            supabase_url="SUPABASE_URL", supabase_key="SUPABASE_KEY"
        )

    def test_get_unauthenticated_client_missing_key(
        self, mock_create_client: Mock, mock_config: Mock
    ) -> None:
        mock_config.SUPABASE.KEY = None
        mock_config.SUPABASE.URL = "SUPABASE_URL"

        with pytest.raises(
            ValueError,
            match="SUPABASE_KEY and SUPABASE_URL must be set in the environment",
        ):
            get_unauthenticated_client()

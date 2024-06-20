from fastapi import Depends
from supabase import Client, create_client

from src.auth.dependencies import get_access_token, get_refresh_token
from src.config import Config


def get_authenticated_client(
    access_token: str = Depends(get_access_token),
    refresh_token: str = Depends(get_refresh_token),
) -> Client:
    if Config.SUPABASE.KEY is None or Config.SUPABASE.URL is None:
        raise ValueError("SUPABASE_KEY and SUPABASE_URL must be set in the environment")
    client = create_client(
        supabase_url=Config.SUPABASE.URL,
        supabase_key=Config.SUPABASE.KEY,
    )
    client.auth.set_session(access_token=access_token, refresh_token=refresh_token)
    return client


def get_unauthenticated_client() -> Client:
    if Config.SUPABASE.KEY is None or Config.SUPABASE.URL is None:
        raise ValueError("SUPABASE_KEY and SUPABASE_URL must be set in the environment")
    return create_client(
        supabase_url=Config.SUPABASE.URL,
        supabase_key=Config.SUPABASE.KEY,
    )


def get_scrapper_client() -> Client:
    if Config.SUPABASE.KEY is None or Config.SUPABASE.URL is None:
        raise ValueError("SUPABASE_KEY and SUPABASE_URL must be set in the environment")
    if (
        Config.SCRAPING.SUPABASE_EMAIL is None
        or Config.SCRAPING.SUPABASE_PASSWORD is None
    ):
        raise ValueError(
            "SUPABASE_SCRAPER_EMAIL and SUPABASE_SCRAPER_PASSWORD must be set in the environment"
        )
    client = create_client(
        supabase_url=Config.SUPABASE.URL,
        supabase_key=Config.SUPABASE.KEY,
    )
    client.auth.sign_in_with_password(
        {
            "email": Config.SCRAPING.SUPABASE_EMAIL,
            "password": Config.SCRAPING.SUPABASE_PASSWORD,
        }
    )
    return client

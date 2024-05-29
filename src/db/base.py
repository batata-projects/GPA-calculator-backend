from supabase import Client, create_client

from src.config import config


def get_authenticated_client() -> Client:
    # TODO: Implement authentication
    return get_unauthenticated_client()


def get_unauthenticated_client() -> Client:
    if config.SUPABASE_KEY is None or config.SUPABASE_URL is None:
        raise ValueError("SUPABASE_KEY and SUPABASE_URL must be set in the environment")
    return create_client(
        supabase_url=config.SUPABASE_URL,
        supabase_key=config.SUPABASE_KEY,
    )

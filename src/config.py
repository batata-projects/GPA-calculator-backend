import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")
    SUPABASE_URL = os.getenv("SUPABASE_URL")


config = Config()

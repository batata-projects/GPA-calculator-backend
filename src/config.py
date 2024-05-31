import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    class APP:
        TITLE = "GPA Calculator"
        DESCRIPTION = "A simple GPA calculator API"
        VERSION = "0.1.0"

    class SUPABASE:
        KEY = os.getenv("SUPABASE_KEY")
        URL = os.getenv("SUPABASE_URL")

    class RANDOM:
        SEED = 0


config = Config()

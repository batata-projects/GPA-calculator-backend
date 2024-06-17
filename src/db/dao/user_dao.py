from supabase import Client

from src.db.dao import BaseDAO
from src.db.models import User
from src.db.tables import SupabaseTables


class UserDAO(BaseDAO[User]):
    def __init__(self, client: Client) -> None:
        super().__init__(client, SupabaseTables.USERS, User)

from supabase import Client

from src.db.dao import BaseDAO
from src.db.models import Term
from src.db.tables import SupabaseTables


class TermDAO(BaseDAO[Term]):
    def __init__(self, client: Client) -> None:
        super().__init__(client, SupabaseTables.TERMS, Term)

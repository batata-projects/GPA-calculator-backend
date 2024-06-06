from supabase import Client

from src.db.models.terms import Term
from src.db.models.utils import TermStr, UuidStr
from src.db.tables import SupabaseTables


class TermDAO:
    def __init__(self, client: Client):
        self.client = client

    def get_term_by_id(self, term_id: UuidStr):
        data = (
            self.client.table(SupabaseTables.TERMS)
            .select("*")
            .eq("id", term_id)
            .execute()
        )
        if not data.data:
            return None
        return Term.model_validate(data.data[0])

    def get_term_by_name(self, name: TermStr):
        data = (
            self.client.table(SupabaseTables.TERMS)
            .select("*")
            .eq("name", name)
            .execute()
        )
        if not data.data:
            return None
        return Term.model_validate(data.data[0])

    def create_term(self, term_data: dict):
        Term.model_validate(term_data)
        data = self.client.table(SupabaseTables.TERMS).insert(term_data).execute()
        if not data.data:
            return None
        return Term.model_validate(data.data[0])

    def update_term(self, term_id: UuidStr, term_data: dict):
        Term.model_validate_partial(term_data)
        data = (
            self.client.table(SupabaseTables.TERMS)
            .update(term_data)
            .eq("id", term_id)
            .execute()
        )
        if not data.data:
            return None
        return Term.model_validate(data.data[0])

    def delete_term(self, term_id: UuidStr):
        data = (
            self.client.table(SupabaseTables.TERMS).delete().eq("id", term_id).execute()
        )
        if not data.data:
            return None
        return Term.model_validate(data.data[0])

    def get_all_terms(self) -> list[Term]:
        data = self.client.table(SupabaseTables.TERMS).select("*").execute()
        if not data.data:
            return []
        return [Term.model_validate(term) for term in data.data]

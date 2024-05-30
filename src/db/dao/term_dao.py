from supabase import Client

from src.db.models.terms import Term
from src.db.models.utils import TermStr
from src.db.tables import SupabaseTables


class TermDAO:
    def __init__(self, client: Client):
        self.client = client

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

    def create_term(self, term: Term):
        data = (
            self.client.table(SupabaseTables.TERMS).insert(term.model_dump()).execute()
        )
        if not data.data:
            return None
        return Term.model_validate(data.data[0])

    def update_term(self, term_name: TermStr):
        self.client.table(SupabaseTables.TERMS).update({"name": term_name}).eq(
            "name", term_name
        ).execute()

    def delete_term(self, term_name: TermStr):
        data = (
            self.client.table(SupabaseTables.TERMS)
            .delete()
            .eq("name", term_name)
            .execute()
        )
        if not data.data:
            return None
        return Term.model_validate(data.data[0])

    def get_all_terms(self) -> list[Term]:
        data = self.client.table(SupabaseTables.TERMS).select("*").execute()
        if not data.data:
            return []
        return [Term.model_validate(term) for term in data.data]

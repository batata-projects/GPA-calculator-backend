from supabase import Client

from src.db.models.terms import Term
from src.db.models.utils.models.BaseModel import BaseModel
from src.db.models.utils.types.TermStr import TermStr
from src.db.models.utils.types.UuidStr import UuidStr
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
        return BaseModel.model_validate_partial(data.data[0])

    def get_term_by_name(self, name: TermStr):
        data = (
            self.client.table(SupabaseTables.TERMS)
            .select("*")
            .eq("name", name)
            .execute()
        )
        if not data.data:
            return None
        return BaseModel.model_validate_partial(data.data[0])

    def create_term(self, term_data: dict):
        BaseModel.model_validate_partial(term_data)
        data = self.client.table(SupabaseTables.TERMS).insert(term_data).execute()
        if not data.data:
            return None
        return BaseModel.model_validate_partial(data.data[0])

    def update_term(self, term_id: UuidStr, term_data: dict):
        BaseModel.model_validate_partial(term_data)
        data = (
            self.client.table(SupabaseTables.TERMS)
            .update(term_data)
            .eq("id", term_id)
            .execute()
        )
        if not data.data:
            return None
        return BaseModel.model_validate_partial(data.data[0])

    def delete_term(self, term_id: UuidStr):
        data = (
            self.client.table(SupabaseTables.TERMS).delete().eq("id", term_id).execute()
        )
        if not data.data:
            return None
        return BaseModel.model_validate_partial(data.data[0])

    def get_all_terms(self) -> list[Term]:
        data = self.client.table(SupabaseTables.TERMS).select("*").execute()
        if not data.data:
            return []
        return [BaseModel.model_validate_partial(term) for term in data.data]

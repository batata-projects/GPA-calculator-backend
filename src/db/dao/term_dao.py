from typing import Optional, Union

from supabase import Client

from src.common.utils.types.TermStr import TermStr
from src.common.utils.types.UuidStr import UuidStr
from src.db.models.terms import Term
from src.db.tables import SupabaseTables


class TermDAO:
    def __init__(self, client: Client) -> None:
        self.client = client

    def get_term_by_id(self, term_id: UuidStr) -> Optional[Term]:
        data = (
            self.client.table(SupabaseTables.TERMS)
            .select("*")
            .eq("id", term_id)
            .execute()
        )
        if not data.data:
            return None
        return Term.model_validate(data.data[0])

    def create_term(
        self, term_data: dict[str, Union[UuidStr, TermStr]]
    ) -> Optional[Term]:
        Term.model_validate(term_data)
        data = self.client.table(SupabaseTables.TERMS).insert(term_data).execute()
        if not data.data:
            return None
        return Term.model_validate(data.data[0])

    def update_term(
        self, term_id: UuidStr, term_data: dict[str, Union[UuidStr, TermStr]]
    ) -> Optional[Term]:
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

    def delete_term(self, term_id: UuidStr) -> Optional[Term]:
        data = (
            self.client.table(SupabaseTables.TERMS).delete().eq("id", term_id).execute()
        )
        if not data.data:
            return None
        return Term.model_validate(data.data[0])

    def get_terms_by_query(
        self,
        id: UuidStr,
        name: TermStr,
    ) -> list[Term]:
        queries = self.client.table(SupabaseTables.TERMS).select("*")
        if id:
            queries = queries.eq("id", id)
        if name:
            queries = queries.eq("name", name)
        data = queries.execute()
        if not data.data:
            return []
        return [Term.model_validate(term) for term in data.data]

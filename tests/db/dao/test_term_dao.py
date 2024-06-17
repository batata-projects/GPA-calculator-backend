from unittest.mock import Mock

from postgrest.base_request_builder import APIResponse
from supabase import Client

from src.db.dao import TermDAO
from src.db.models import Term
from src.db.tables import SupabaseTables


class TestTermDAO:
    def test_get_term_by_id_successful(self, terms: list[Term]) -> None:
        term = terms[0]
        mock_client = Mock(spec=Client)
        term_dao = TermDAO(mock_client)

        mock_client.table(SupabaseTables.TERMS).select("*").eq(
            "id", term.id
        ).execute.return_value = APIResponse(data=[term.model_dump()], count=None)

        assert term.id is not None

        result = term_dao.get_by_id(term.id)

        assert result == term

    def test_create_term_successful(self, terms: list[Term]) -> None:
        term = terms[0]
        mock_client = Mock(spec=Client)
        term_dao = TermDAO(mock_client)

        mock_client.table(SupabaseTables.TERMS).insert(
            term.model_dump()
        ).execute.return_value = APIResponse(data=[term.model_dump()], count=None)

        result = term_dao.create(term.model_dump())

        assert result == term

    def test_update_term_successful(self, terms: list[Term]) -> None:
        term = terms[0]
        mock_client = Mock(spec=Client)
        term_dao = TermDAO(mock_client)

        mock_client.table(SupabaseTables.TERMS).update(term.model_dump()).eq(
            "id", term.id
        ).execute.return_value = APIResponse(data=[term.model_dump()], count=None)

        assert term.id is not None

        result = term_dao.update(term.id, term.model_dump())

        assert result == term

    def test_delete_term_successful(self, terms: list[Term]) -> None:
        term = terms[0]
        mock_client = Mock(spec=Client)
        term_dao = TermDAO(mock_client)

        mock_client.table(SupabaseTables.TERMS).delete().eq(
            "id", term.id
        ).execute.return_value = APIResponse(data=[term.model_dump()], count=None)

        assert term.id is not None

        result = term_dao.delete(term.id)

        assert result == term

    def test_get_term_by_query_successful(self, terms: list[Term]) -> None:
        term = terms[0]
        mock_client = Mock(spec=Client)
        term_dao = TermDAO(mock_client)

        mock_client.table(SupabaseTables.TERMS).select("*").eq("id", term.id).eq(
            "name", term.name
        ).execute.return_value = APIResponse(data=[term.model_dump()], count=None)

        assert term.id is not None

        result = term_dao.get_by_query(id=term.id, name=term.name)

        assert result == [term]

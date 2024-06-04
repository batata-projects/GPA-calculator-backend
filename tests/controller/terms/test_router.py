from unittest.mock import Mock

import pytest
from fastapi import status

from src.controller.terms.router import get_term_by_id
from src.controller.terms.schemas import TermResponse
from src.db.dao.term_dao import TermDAO
from src.db.models.terms import Term


@pytest.mark.asyncio
class TestGetTermById:
    async def test_get_term_by_id_successful(self, term1: Term):
        term_dao = Mock(spec=TermDAO)
        term_dao.get_term_by_id.return_value = term1

        assert term1.id is not None

        response = await get_term_by_id(term_id=term1.id, term_dao=term_dao)

        assert response.status == status.HTTP_200_OK
        assert response.message == "Term found"
        assert response.data == TermResponse(terms=[term1])

    async def test_get_term_by_id_not_found(self, uuid4: Mock):
        term_dao = Mock(spec=TermDAO)
        term_dao.get_term_by_id.return_value = None

        response = await get_term_by_id(term_id=str(uuid4()), term_dao=term_dao)

        assert response.status == status.HTTP_404_NOT_FOUND
        assert response.message == "Term not found"
        assert response.data is None

    async def test_get_term_by_id_error(self, uuid4: Mock):
        term_dao = Mock(spec=TermDAO)
        term_dao.get_term_by_id.side_effect = Exception("Error")

        response = await get_term_by_id(term_id=str(uuid4()), term_dao=term_dao)

        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Error"
        assert response.data is None


class TestGetTermByName: ...


class TestCreateTerm: ...


class TestUpdateTerm: ...


class TestDeleteTerm: ...


class TestGetAllTerms: ...

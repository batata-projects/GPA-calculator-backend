from unittest.mock import Mock

import pytest
from fastapi import status

from src.controller.terms.router import (
    create_term,
    delete_term,
    get_all_terms,
    get_term_by_id,
    get_term_by_name,
    update_term,
)
from src.controller.terms.schemas import TermResponse
from src.db.dao.term_dao import TermDAO
from src.db.models.terms import Term


@pytest.mark.asyncio
class TestGetTermById:
    async def test_get_term_by_id_successful(self, term1: Term) -> None:
        term_dao = Mock(spec=TermDAO)
        term_dao.get_term_by_id.return_value = term1

        assert term1.id is not None

        response = await get_term_by_id(term_id=term1.id, term_dao=term_dao)

        assert response.status == status.HTTP_200_OK
        assert response.message == "Term found"
        assert response.data == TermResponse(terms=[term1])

    async def test_get_term_by_id_not_found(self, uuid4: Mock) -> None:
        term_dao = Mock(spec=TermDAO)
        term_dao.get_term_by_id.return_value = None

        response = await get_term_by_id(term_id=str(uuid4()), term_dao=term_dao)

        assert response.status == status.HTTP_404_NOT_FOUND
        assert response.message == "Term not found"
        assert response.data is None

    async def test_get_term_by_id_error(self, uuid4: Mock) -> None:
        term_dao = Mock(spec=TermDAO)
        term_dao.get_term_by_id.side_effect = Exception("Error")

        response = await get_term_by_id(term_id=str(uuid4()), term_dao=term_dao)

        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Error"
        assert response.data is None


@pytest.mark.asyncio
class TestGetTermByName:
    async def test_get_term_by_name_successful(self, term1: Term) -> None:
        term_dao = Mock(spec=TermDAO)
        term_dao.get_term_by_name.return_value = term1

        assert term1.name is not None

        response = await get_term_by_name(term_name=term1.name, term_dao=term_dao)

        assert response.status == status.HTTP_200_OK
        assert response.message == "Term found"
        assert response.data == TermResponse(terms=[term1])

    async def test_get_term_by_name_not_found(self) -> None:
        term_dao = Mock(spec=TermDAO)
        term_dao.get_term_by_name.return_value = None

        response = await get_term_by_name(
            term_name="Fall 2023 - 2024", term_dao=term_dao
        )

        assert response.status == status.HTTP_404_NOT_FOUND
        assert response.message == "Term not found"
        assert response.data is None

    async def test_get_term_by_name_error(self) -> None:
        term_dao = Mock(spec=TermDAO)
        term_dao.get_term_by_name.side_effect = Exception("Error")

        response = await get_term_by_name(
            term_name="Fall 2023 - 2024", term_dao=term_dao
        )

        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Error"
        assert response.data is None


@pytest.mark.asyncio
class TestCreateTerm:
    async def test_create_term_successful(self, term1: Term) -> None:
        term_dao = Mock(spec=TermDAO)
        term_dao.create_term.return_value = term1

        assert term1.name is not None

        response = await create_term(term_name=term1.name, term_dao=term_dao)

        assert response.status == status.HTTP_201_CREATED
        assert response.message == "Term created"
        assert response.data == TermResponse(terms=[term1])

    async def test_create_term_duplicate(self) -> None:
        term_dao = Mock(spec=TermDAO)
        term_dao.create_term.side_effect = Exception("Failed to create term")

        response = await create_term(term_name="Fall 2022 - 2023", term_dao=term_dao)

        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Failed to create term"
        assert response.data is None

    async def test_create_term_error(self) -> None:
        term_dao = Mock(spec=TermDAO)
        term_dao.create_term.side_effect = Exception("Error")

        response = await create_term(term_name="Fall 2022 - 2023", term_dao=term_dao)

        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Error"
        assert response.data is None


@pytest.mark.asyncio
class TestUpdateTerm:
    async def test_update_term_successful(self, term1: Term) -> None:
        term_dao = Mock(spec=TermDAO)
        term1.name = "Fall 2026 - 2027"
        term_dao.update_term.return_value = term1

        assert term1.id is not None

        response = await update_term(
            term_id=term1.id, term_name="Fall 2026 - 2027", term_dao=term_dao
        )

        assert response.status == status.HTTP_200_OK
        assert response.message == "Term updated"
        assert response.data == TermResponse(terms=[term1])

    async def test_update_term_not_found(self, uuid4: Mock, term1: Term) -> None:
        term_dao = Mock(spec=TermDAO)
        term_dao.update_term.return_value = None

        response = await update_term(
            term_id=str(uuid4()), term_name=term1.name, term_dao=term_dao
        )

        assert response.status == status.HTTP_400_BAD_REQUEST
        assert response.message == "Failed to update term"
        assert response.data is None

    async def test_update_term_duplicate(self, term1: Term, term2: Term) -> None:
        term_dao = Mock(spec=TermDAO)
        term_dao.update_term.side_effect = Exception("Failed to update term")

        assert term1.id is not None

        response = await update_term(
            term_id=term1.id, term_name=term2.name, term_dao=term_dao
        )

        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Failed to update term"
        assert response.data is None


@pytest.mark.asyncio
class TestDeleteTerm:
    async def test_delete_term_successful(self, term1: Term) -> None:
        term_dao = Mock(spec=TermDAO)
        term_dao.delete_term.return_value = term1

        assert term1.id is not None

        response = await delete_term(term_id=term1.id, term_dao=term_dao)

        assert response.status == status.HTTP_200_OK
        assert response.message == "Term deleted"
        assert response.data == TermResponse(terms=[term1])

    async def test_delete_term_not_found(self, uuid4: Mock) -> None:
        term_dao = Mock(spec=TermDAO)
        term_dao.delete_term.return_value = None

        response = await delete_term(term_id=str(uuid4()), term_dao=term_dao)

        assert response.status == status.HTTP_400_BAD_REQUEST
        assert response.message == "Failed to delete term"
        assert response.data is None

    async def test_delete_term_error(self, uuid4: Mock) -> None:
        term_dao = Mock(spec=TermDAO)
        term_dao.delete_term.side_effect = Exception("Error")

        response = await delete_term(term_id=str(uuid4()), term_dao=term_dao)

        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Error"
        assert response.data is None


@pytest.mark.asyncio
class TestGetAllTerms:
    async def test_get_all_terms_successful(self, terms: list[Term]) -> None:
        term_dao = Mock(spec=TermDAO)
        term_dao.get_all_terms.return_value = terms

        response = await get_all_terms(term_dao=term_dao)

        assert response.status == status.HTTP_200_OK
        assert response.message == "Terms found"
        assert response.data == TermResponse(terms=terms)

    async def test_get_all_terms_unsuccessful(self) -> None:
        term_dao = Mock(spec=TermDAO)
        term_dao.get_all_terms.return_value = []

        response = await get_all_terms(term_dao=term_dao)

        assert response.status == status.HTTP_404_NOT_FOUND
        assert response.message == "No terms found"
        assert response.data is None

    async def test_get_all_terms_error(self) -> None:
        term_dao = Mock(spec=TermDAO)
        term_dao.get_all_terms.side_effect = Exception("Error")

        response = await get_all_terms(term_dao=term_dao)

        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Error"
        assert response.data is None

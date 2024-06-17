from unittest.mock import Mock

import pytest
from fastapi import status

from src.controller.available_courses import (
    AvailableCourseRequest,
    AvailableCourseResponse,
)
from src.controller.available_courses.router import (
    create_available_course,
    delete_available_course,
    get_available_course_by_id,
    get_available_courses_by_query,
    update_available_course,
)
from src.db.dao import AvailableCourseDAO
from src.db.models import AvailableCourse


@pytest.mark.asyncio
class TestGetAvailableCourseById:
    async def test_get_available_course_by_id_successful(
        self, available_course1: AvailableCourse
    ) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.get_by_id.return_value = available_course1

        assert available_course1.id is not None

        response = await get_available_course_by_id(
            available_course_id=available_course1.id,
            available_course_dao=available_course_dao,
        )

        assert response.status == status.HTTP_200_OK
        assert response.message == "Available course found"
        assert response.data == AvailableCourseResponse(items=[available_course1])

    async def test_get_available_course_by_id_not_found(self, valid_uuid: Mock) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.get_by_id.return_value = None

        response = await get_available_course_by_id(
            available_course_id=str(valid_uuid),
            available_course_dao=available_course_dao,
        )

        assert response.status == status.HTTP_404_NOT_FOUND
        assert response.message == "Available course not found"
        assert response.data is None

    async def test_get_available_course_by_id_error(self, valid_uuid: Mock) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.get_by_id.side_effect = Exception("Error")

        response = await get_available_course_by_id(
            available_course_id=str(valid_uuid),
            available_course_dao=available_course_dao,
        )

        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Error"
        assert response.data is None


@pytest.mark.asyncio
class TestGetAvailableCoursesByQuery:
    async def test_get_available_courses_by_query_successful(
        self, available_course1: AvailableCourse
    ) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.get_by_query.return_value = [available_course1]

        response = await get_available_courses_by_query(
            term_id=available_course1.term_id, available_course_dao=available_course_dao
        )

        assert response.status == status.HTTP_200_OK
        assert response.message == "Available courses found"
        assert response.data == AvailableCourseResponse(items=[available_course1])

    async def test_get_available_courses_by_query_not_found(
        self, available_course1: AvailableCourse
    ) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.get_by_query.return_value = None

        response = await get_available_courses_by_query(
            term_id=available_course1.term_id, available_course_dao=available_course_dao
        )

        assert response.status == status.HTTP_404_NOT_FOUND
        assert response.message == "Available courses not found"
        assert response.data == None

    async def test_get_available_courses_by_query_error(
        self, available_course1: AvailableCourse
    ) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.get_by_query.side_effect = Exception("Error")

        response = await get_available_courses_by_query(
            term_id=available_course1.term_id, available_course_dao=available_course_dao
        )

        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Error"
        assert response.data == None


@pytest.mark.asyncio
class TestCreateAvailableCourse:
    async def test_create_available_course_successful(
        self,
        available_course1: AvailableCourse,
        available_course_request: AvailableCourseRequest,
    ) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.create.return_value = available_course1

        response = await create_available_course(
            available_course_request,
            available_course_dao=available_course_dao,
        )

        assert response.status == status.HTTP_201_CREATED
        assert response.message == "Available course created"
        assert response.data == AvailableCourseResponse(items=[available_course1])

    async def test_create_available_course_error(
        self, available_course_request: AvailableCourseRequest
    ) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.create.side_effect = Exception("Error")

        response = await create_available_course(
            available_course_request, available_course_dao
        )

        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Error"
        assert response.data == None


@pytest.mark.asyncio
class TestUpdateAvailableCourse:
    async def test_update_available_course_successful(
        self, available_course1: AvailableCourse
    ) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.update.return_value = available_course1
        assert available_course1.id is not None
        response = await update_available_course(
            available_course1.id,
            available_course1.term_id,
            available_course1.name,
            available_course1.code,
            available_course1.credits,
            available_course1.graded,
            available_course_dao=available_course_dao,
        )

        assert response.status == status.HTTP_200_OK
        assert response.message == "Available course updated"
        assert response.data == AvailableCourseResponse(items=[available_course1])

    async def test_update_available_course_id_not_found(self, valid_uuid: Mock) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.update.return_value = None

        response = await update_available_course(
            str(valid_uuid),
            "Fall 2022 - 2023",
            available_course_dao=available_course_dao,
        )

        assert response.status == status.HTTP_404_NOT_FOUND
        assert response.message == "Available course not updated"
        assert response.data == None

    async def test_update_available_course_error(
        self, available_course1: AvailableCourse
    ) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.update.side_effect = Exception("Error")
        assert available_course1.id is not None
        response = await update_available_course(
            available_course1.id,
            available_course1.term_id,
            available_course1.name,
            available_course1.code,
            available_course1.credits,
            available_course1.graded,
            available_course_dao=available_course_dao,
        )

        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Error"
        assert response.data == None


@pytest.mark.asyncio
class TestDeleteAvailableCourse:
    async def test_delete_available_course_successful(
        self, available_course1: AvailableCourse
    ) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.delete.return_value = available_course1
        assert available_course1.id is not None
        response = await delete_available_course(
            available_course1.id, available_course_dao=available_course_dao
        )

        assert response.status == status.HTTP_200_OK
        assert response.message == "Available course deleted"
        assert response.data == AvailableCourseResponse(items=[available_course1])

    async def test_delete_available_course_id_not_found(self, valid_uuid: Mock) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.delete.return_value = None

        response = await delete_available_course(
            str(valid_uuid), available_course_dao=available_course_dao
        )

        assert response.status == status.HTTP_404_NOT_FOUND
        assert response.message == "Available course not deleted"
        assert response.data == None

    async def test_delete_available_course_error(
        self, available_course1: AvailableCourse
    ) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.delete.side_effect = Exception("Error")
        assert available_course1.id is not None
        response = await delete_available_course(
            available_course1.id, available_course_dao=available_course_dao
        )

        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Error"
        assert response.data == None

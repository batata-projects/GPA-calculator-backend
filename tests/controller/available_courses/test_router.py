from unittest.mock import Mock

import pytest
from fastapi import status

from src.controller.available_courses.router import (
    create_available_course,
    delete_available_course,
    get_all_available_courses,
    get_available_course_by_id,
    get_available_courses_by_course_name,
    get_available_courses_by_credit,
    get_available_courses_by_graded,
    get_available_courses_by_terms_id,
    update_available_course,
)
from src.controller.available_courses.schemas import AvailableCourseResponse
from src.db.dao.available_course_dao import AvailableCourseDAO
from src.db.models.available_courses import AvailableCourse


@pytest.mark.asyncio
class TestGetAvailableCourseById:
    async def test_get_available_course_by_id_successful(
        self, available_course1: AvailableCourse
    ) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.get_available_course_by_id.return_value = available_course1

        assert available_course1.id is not None

        response = await get_available_course_by_id(
            available_course_id=available_course1.id,
            available_course_dao=available_course_dao,
        )

        assert response.status == status.HTTP_200_OK
        assert response.message == "Available course found"
        assert response.data == AvailableCourseResponse(
            available_courses=[available_course1]
        )

    async def test_get_available_course_by_id_not_found(self, uuid4: Mock) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.get_available_course_by_id.return_value = None

        response = await get_available_course_by_id(
            available_course_id=str(uuid4()), available_course_dao=available_course_dao
        )

        assert response.status == status.HTTP_404_NOT_FOUND
        assert response.message == "Available course not found"
        assert response.data is None

    async def test_get_available_course_by_id_error(self, uuid4: Mock) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.get_available_course_by_id.side_effect = Exception("Error")

        response = await get_available_course_by_id(
            available_course_id=str(uuid4()), available_course_dao=available_course_dao
        )

        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Error"
        assert response.data is None


@pytest.mark.asyncio
class TestGetAvailableCoursesByCourseName:
    async def test_get_available_courses_by_course_name_successful(
        self, available_course1: AvailableCourse
    ) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.get_available_courses_by_course_name.return_value = [
            available_course1
        ]

        assert available_course1.name is not None

        response = await get_available_courses_by_course_name(
            course_name=available_course1.name,
            available_course_dao=available_course_dao,
        )

        assert response.status == status.HTTP_200_OK
        assert response.message == "Available courses found"
        assert response.data == AvailableCourseResponse(
            available_courses=[available_course1]
        )

    async def test_get_available_courses_by_course_name_not_found(self) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.get_available_courses_by_course_name.return_value = None

        response = await get_available_courses_by_course_name(
            course_name="Arol", available_course_dao=available_course_dao
        )

        assert response.status == status.HTTP_404_NOT_FOUND
        assert response.message == "Available courses not found"
        assert response.data == None

    async def test_get_available_courses_by_course_name_error(self) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.get_available_courses_by_course_name.side_effect = (
            Exception("Error")
        )

        response = await get_available_courses_by_course_name(
            course_name="Arol", available_course_dao=available_course_dao
        )

        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Error"
        assert response.data == None


@pytest.mark.asyncio
class TestGetAvailableCoursesByCredit:
    async def test_get_available_courses_by_credit_successful(
        self, available_course1: AvailableCourse
    ) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.get_available_courses_by_credit.return_value = [
            available_course1
        ]

        assert available_course1.credits is not None

        response = await get_available_courses_by_credit(
            credit=available_course1.credits, available_course_dao=available_course_dao
        )

        assert response.status == status.HTTP_200_OK
        assert response.message == "Available courses found"
        assert response.data == AvailableCourseResponse(
            available_courses=[available_course1]
        )

    async def test_get_available_courses_by_credit_not_found(self) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.get_available_courses_by_credit.return_value = None

        response = await get_available_courses_by_credit(
            credit=3, available_course_dao=available_course_dao
        )

        assert response.status == status.HTTP_404_NOT_FOUND
        assert response.message == "Available courses not found"
        assert response.data == None

    async def test_get_available_courses_by_credit_error(self) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.get_available_courses_by_credit.side_effect = Exception(
            "Error"
        )

        response = await get_available_courses_by_credit(
            credit=3, available_course_dao=available_course_dao
        )

        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Error"
        assert response.data == None


@pytest.mark.asyncio
class TestGetAvailableCoursesByTermsId:
    async def test_get_available_courses_by_terms_id_successful(
        self, available_course1: AvailableCourse
    ) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.get_available_courses_by_term_id.return_value = [
            available_course1
        ]

        assert available_course1.term_id is not None

        response = await get_available_courses_by_terms_id(
            term_id=available_course1.term_id, available_course_dao=available_course_dao
        )

        assert response.status == status.HTTP_200_OK
        assert response.message == "Available courses found"
        assert response.data == AvailableCourseResponse(
            available_courses=[available_course1]
        )

    async def test_get_available_courses_by_terms_id_not_found(
        self, uuid4: Mock
    ) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.get_available_courses_by_term_id.return_value = None

        response = await get_available_courses_by_terms_id(
            term_id=str(uuid4()), available_course_dao=available_course_dao
        )

        assert response.status == status.HTTP_404_NOT_FOUND
        assert response.message == "Available courses not found"
        assert response.data == None

    async def test_get_available_courses_by_terms_id_error(self, uuid4: Mock) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.get_available_courses_by_term_id.side_effect = Exception(
            "Error"
        )

        response = await get_available_courses_by_terms_id(
            term_id=str(uuid4()), available_course_dao=available_course_dao
        )

        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Error"
        assert response.data == None


@pytest.mark.asyncio
class TestGetAvailableCoursesByGraded:
    async def test_get_available_courses_by_graded_successful(
        self, available_course1: AvailableCourse
    ) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.get_available_courses_by_graded.return_value = [
            available_course1
        ]

        assert available_course1.graded is not None

        response = await get_available_courses_by_graded(
            graded=available_course1.graded, available_course_dao=available_course_dao
        )

        assert response.status == status.HTTP_200_OK
        assert response.message == "Available courses found"
        assert response.data == AvailableCourseResponse(
            available_courses=[available_course1]
        )

    async def test_get_available_courses_by_graded_not_found(self) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.get_available_courses_by_graded.return_value = None

        response = await get_available_courses_by_graded(
            graded=False, available_course_dao=available_course_dao
        )

        assert response.status == status.HTTP_404_NOT_FOUND
        assert response.message == "Available courses not found"
        assert response.data == None

    async def test_get_available_courses_by_graded_error(self) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.get_available_courses_by_graded.side_effect = Exception(
            "Error"
        )

        response = await get_available_courses_by_graded(
            graded=False, available_course_dao=available_course_dao
        )

        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Error"
        assert response.data == None


@pytest.mark.asyncio
class TestGetAllAvailableCourses:
    async def test_get_all_available_courses_successful(
        self, available_course1: AvailableCourse
    ) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.get_all_available_courses.return_value = [
            available_course1
        ]

        response = await get_all_available_courses(
            available_course_dao=available_course_dao
        )

        assert response.status == status.HTTP_200_OK
        assert response.message == "Available courses found"
        assert response.data == AvailableCourseResponse(
            available_courses=[available_course1]
        )

    async def test_get_all_available_courses_not_found(self) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.get_all_available_courses.return_value = None

        response = await get_all_available_courses(
            available_course_dao=available_course_dao
        )

        assert response.status == status.HTTP_404_NOT_FOUND
        assert response.message == "Available courses not found"
        assert response.data == None

    async def test_get_all_available_courses_error(self) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.get_all_available_courses.side_effect = Exception("Error")

        response = await get_all_available_courses(
            available_course_dao=available_course_dao
        )

        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Error"
        assert response.data == None


@pytest.mark.asyncio
class TestCreateAvailableCourse:
    async def test_create_available_course_successful(
        self, available_course1: AvailableCourse
    ) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.create_available_course.return_value = available_course1

        response = await create_available_course(
            available_course1.term_id,
            available_course1.name,
            available_course1.code,
            available_course1.credits,
            available_course1.graded,
            available_course_dao=available_course_dao,
        )

        assert response.status == status.HTTP_201_CREATED
        assert response.message == "Available course created"
        assert response.data == AvailableCourseResponse(
            available_courses=[available_course1]
        )

    async def test_create_available_course_error(
        self, available_course1: AvailableCourse
    ) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.create_available_course.side_effect = Exception("Error")

        response = await create_available_course(
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
class TestUpdateAvailableCourse:
    async def test_update_available_course_successful(
        self, available_course1: AvailableCourse
    ) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.update_available_course.return_value = available_course1
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
        assert response.data == AvailableCourseResponse(
            available_courses=[available_course1]
        )

    async def test_update_available_course_id_not_found(self, uuid4: Mock) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.update_available_course.return_value = None

        response = await update_available_course(
            str(uuid4()), "Fall 2022 - 2023", available_course_dao=available_course_dao
        )

        assert response.status == status.HTTP_404_NOT_FOUND
        assert response.message == "Available course not updated"
        assert response.data == None

    async def test_update_available_course_error(
        self, available_course1: AvailableCourse
    ) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.update_available_course.side_effect = Exception("Error")
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
        available_course_dao.delete_available_course.return_value = available_course1
        assert available_course1.id is not None
        response = await delete_available_course(
            available_course1.id, available_course_dao=available_course_dao
        )

        assert response.status == status.HTTP_200_OK
        assert response.message == "Available course deleted"
        assert response.data == AvailableCourseResponse(
            available_courses=[available_course1]
        )

    async def test_delete_available_course_id_not_found(self, uuid4: Mock) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.delete_available_course.return_value = None

        response = await delete_available_course(
            str(uuid4()), available_course_dao=available_course_dao
        )

        assert response.status == status.HTTP_404_NOT_FOUND
        assert response.message == "Available course not deleted"
        assert response.data == None

    async def test_delete_available_course_error(
        self, available_course1: AvailableCourse
    ) -> None:
        available_course_dao = Mock(spec=AvailableCourseDAO)
        available_course_dao.delete_available_course.side_effect = Exception("Error")
        assert available_course1.id is not None
        response = await delete_available_course(
            available_course1.id, available_course_dao=available_course_dao
        )

        assert response.status == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.message == "Error"
        assert response.data == None

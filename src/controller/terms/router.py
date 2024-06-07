from fastapi import APIRouter, Depends, Path, Query, status

from src.common.responses import APIResponse
from src.common.utils.types.TermStr import TermStr
from src.common.utils.types.UuidStr import UuidStr
from src.controller.terms.schemas import TermResponse
from src.db.dao.term_dao import TermDAO
from src.db.dependencies import get_term_dao

router = APIRouter(
    prefix="/terms",
    tags=["terms"],
)


@router.get(
    "/{term_id}",
    response_model=APIResponse[TermResponse],
    response_description="Get term by ID",
)
async def get_term_by_id(
    term_id: UuidStr = Path(..., description="Term ID"),
    term_dao: TermDAO = Depends(get_term_dao),
) -> APIResponse[TermResponse]:
    try:
        term = term_dao.get_term_by_id(term_id)
        if term:
            return APIResponse[TermResponse](
                status=status.HTTP_200_OK,
                message="Term found",
                data=TermResponse(terms=[term]),
            )
        return APIResponse(
            status=status.HTTP_404_NOT_FOUND,
            message="Term not found",
        )
    except Exception as e:
        return APIResponse(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e),
        )


@router.get(
    "/{term_name}",
    response_model=APIResponse[TermResponse],
    response_description="Get term by name",
)
async def get_term_by_name(
    term_name: TermStr = Path(..., description="Term name"),
    term_dao: TermDAO = Depends(get_term_dao),
) -> APIResponse[TermResponse]:
    try:
        term = term_dao.get_term_by_name(term_name)
        if term:
            return APIResponse[TermResponse](
                status=status.HTTP_200_OK,
                message="Term found",
                data=TermResponse(terms=[term]),
            )
        return APIResponse(
            status=status.HTTP_404_NOT_FOUND,
            message="Term not found",
        )
    except Exception as e:
        return APIResponse(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e),
        )


@router.post(
    "/",
    response_model=APIResponse[TermResponse],
    response_description="Create a new term",
)
async def create_term(
    term_name: TermStr = Query(..., description="Term name"),
    term_dao: TermDAO = Depends(get_term_dao),
) -> APIResponse[TermResponse]:
    try:
        term_data = {"name": term_name}
        term = term_dao.create_term(term_data)
        if term:
            return APIResponse[TermResponse](
                status=status.HTTP_201_CREATED,
                message="Term created",
                data=TermResponse(terms=[term]),
            )
        return APIResponse(
            status=status.HTTP_400_BAD_REQUEST,
            message="Failed to create term",
        )
    except Exception as e:
        return APIResponse(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e),
        )


@router.put(
    "/{term_id}",
    response_model=APIResponse[TermResponse],
    response_description="Update a term",
)
async def update_term(
    term_id: UuidStr = Path(..., description="Term ID"),
    term_name: TermStr = Query(..., description="Term name"),
    term_dao: TermDAO = Depends(get_term_dao),
) -> APIResponse[TermResponse]:
    try:
        term_data = {"name": term_name}
        term = term_dao.update_term(term_id, term_data)
        if term:
            return APIResponse[TermResponse](
                status=status.HTTP_200_OK,
                message="Term updated",
                data=TermResponse(terms=[term]),
            )
        return APIResponse(
            status=status.HTTP_400_BAD_REQUEST,
            message="Failed to update term",
        )
    except Exception as e:
        return APIResponse(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e),
        )


@router.delete(
    "/{term_id}",
    response_model=APIResponse[TermResponse],
    response_description="Delete a term",
)
async def delete_term(
    term_id: UuidStr = Path(..., description="Term ID"),
    term_dao: TermDAO = Depends(get_term_dao),
) -> APIResponse[TermResponse]:
    try:
        term = term_dao.delete_term(term_id)
        if term:
            return APIResponse[TermResponse](
                status=status.HTTP_200_OK,
                message="Term deleted",
                data=TermResponse(terms=[term]),
            )
        return APIResponse(
            status=status.HTTP_400_BAD_REQUEST,
            message="Failed to delete term",
        )
    except Exception as e:
        return APIResponse(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e),
        )


@router.get(
    "/",
    response_model=APIResponse[TermResponse],
    response_description="Get all terms",
)
async def get_all_terms(
    term_dao: TermDAO = Depends(get_term_dao),
) -> APIResponse[TermResponse]:
    try:
        terms = term_dao.get_all_terms()
        if terms:
            return APIResponse[TermResponse](
                status=status.HTTP_200_OK,
                message="Terms found",
                data=TermResponse(terms=terms),
            )
        return APIResponse(
            status=status.HTTP_404_NOT_FOUND,
            message="No terms found",
        )
    except Exception as e:
        return APIResponse(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e),
        )

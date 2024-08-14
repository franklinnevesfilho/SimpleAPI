from franklin_fastapi_extension import GET, POST, PUT, request, Query
from .mock_dto import MockDTO, ValidationTest
from .mock_service import get_all, post_request


@GET("/get")
async def get_mock_router():
    return await request.get_all(get_all)


@POST("/post")
async def post_mock_router(mock_dto: Query):
    return await request.call(post_request, mock_dto, MockDTO)

@POST("/post/validate")
async def post_mock_router_validate(mock_dto: Query):
    return await request.call(post_request, mock_dto, ValidationTest)


@PUT("/put")
async def put_mock_router(mock_dto: Query):
    return await request.call(post_request, mock_dto, MockDTO)


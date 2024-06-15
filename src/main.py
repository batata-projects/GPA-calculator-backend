from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from src.auth.router import router as auth_router
from src.common.responses import APIResponse
from src.config import Config
from src.controller import (
    available_courses_router,
    courses_router,
    status_router,
    terms_router,
    users_router,
)

app = FastAPI(
    title=Config.APP.TITLE,
    description=Config.APP.DESCRIPTION,
    version=Config.APP.VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router)
app.include_router(available_courses_router)
app.include_router(courses_router)
app.include_router(status_router)
app.include_router(terms_router)
app.include_router(users_router)


@app.get("/")
async def root() -> APIResponse[None]:
    return APIResponse[None](
        message="Welcome to the GPA calculator API", status=status.HTTP_200_OK
    )

from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from src.auth.router import router as auth_router
from src.common.responses import APIResponse
from src.config import Config
from src.controller.available_courses.router import router as available_courses_router
from src.controller.courses.router import router as courses_router
from src.controller.status import router as status_router
from src.controller.terms.router import router as terms_router
from src.controller.users.router import router as users_router

app = FastAPI(
    title=Config.APP.TITLE,
    description=Config.APP.DESCRIPTION,
    version=Config.APP.VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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
async def root():
    return APIResponse(
        message="Welcome to the GPA calculator API", status=status.HTTP_200_OK
    )
